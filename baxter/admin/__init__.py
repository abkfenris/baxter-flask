"""
Admin interface, sets up admin views
"""
import os
import os.path as op

from flask import url_for, redirect
from flask.ext.admin import Admin, AdminIndexView, expose
#from flask.ext.admin.contrib.sqla import ModelView
from flask.ext.admin.contrib.geoa import ModelView
from wtforms.fields import SelectField
from sqlalchemy.event import listens_for
from flask.ext.admin.form import FileUploadField, ImageUploadField, thumbgen_filename
from flask.ext.admin.model import InlineFormAdmin
from flask.ext.security import roles_required, roles_accepted, current_user, login_required
from jinja2 import Markup

from .. import db
from ..models import User, WeatherOb, WeatherFor, Trail, POI, AvalanchePath, AvalancheIn, AvalancheInvolved, Photo, SnowPit

# File path
file_path = op.join(op.dirname(__file__), 'files')
try:
    os.mkdir(file_path)
except OSError:
    pass

# Delete Hook for SnowPit, delete file if model is deleted
@listens_for(SnowPit, 'after_delete')
def del_snowpit(mapper, connection, target):
    if target.path:
        try:
            os.remove(op.join(file_path, target.path))
        except OSError:
            # Don't care as it doesn't exist
            pass

@listens_for(Photo, 'after_delete')
def del_photo(mapper, connection, target):
    if target.path:
        # Delete Image
        try:
            os.remove(op.join(file_path, target.path))
        except OSError:
            pass
        
        # Delete the thumbnail
        try:
            os.remove(op.join(file_path, thumbgen_filename(target.path)))
        except OSError:
            pass



class FileView(ModelView):
    form_overrides = {'path': FileUploadField}
    form_args = {'path': {'label': 'File',
                          'base_path': file_path}}

class InlineFileView(InlineFormAdmin):
    form_overrides = {'path': FileUploadField}
    form_args = {'path': {'label': 'File',
                          'base_path': file_path}}

class ImageView(ModelView):
    #def _list_thumbnail(view, contex, model, name):
    #    if not model.path:
    #        return ''
    #    
    #    return Markup('<img src="%s">' % url_for('admin.static', filename=thumbgen_filename(model.path)))
    
    #column_formatters = {
    #    'path': _list_thumbnail
    #}
    form_extra_fields = {
        'path': ImageUploadField('Photo',
                                base_path=file_path, 
                                thumbnail_size=(100,100, True))
    }

class InlineImageView(InlineFormAdmin):
    form_overrides = {'path': ImageUploadField}
    form_args = {'path': {'label': 'Photo',
                          'base_path': file_path}}
    #form_extra_fields = {
    #    'path': ImageUploadField('Photo',
    #                            base_path=file_path, 
    #                            thumbnail_size=(100,100, True))
    #}



class UserView(ModelView):
	def is_accessible(self):
		return current_user.has_role('admin')
	

# http://wtforms.readthedocs.org/en/latest/ext.html#module-wtforms.ext.sqlalchemy
def observers():
	return User.query.filter_by(observer=True)


class WeatherObView(ModelView):
	form_overrides = dict(sky=SelectField, 
						  precip_type=SelectField, 
						  precip_rate=SelectField,
						  temp_trend=SelectField,
						  pressure_trend=SelectField,
						  wind_direction=SelectField)
	form_args = dict(
		# Pass the choices to the SelectField
		observer=dict(query_factory=observers),
		sky=dict(
			choices=[('CLR', 'Clear'), 
					 ('FEW', 'Few Clouds'), 
					 ('SCT', 'Scattered Clouds'),
					 ('BKN', 'Broken Clouds'),
					 ('OVC', 'Overcast'),
					 ('X', 'Obscured')
					]
		),
		precip_type=dict(
			choices=[('NO', 'No Percipitation'),
					 ('RA', 'Rain'),
					 ('SN', 'Snow'),
					 ('RS', 'Mixed Rain and Snow'),
					 ('GR', 'Gaupel and Hail'),
					 ('ZR', 'Freezing Rain')
					]
		),
		precip_rate=dict(
			choices=[('NO', 'No Precipitation'),
					 ('S-1', 'S-1 - Very Light Snowfall (trace to .25in)'),
					 ('S1', 'S1 - Light Snowfall (.5 in)'),
					 ('S2', 'S2 - Moderate Snowfall (1 in)' ),
					 ('S5', 'S5 - Heavy Snowfall (2 in)' ),
					 ('S10', 'S10 - Very Heavy Snowfall (4 in)'),
					 ('RV', 'RV - Very Light Rain (no accumulation)'),
					 ('RL', 'RL - Light Rain'),
					 ('RM', 'RM - Moderate Rain'),
					 ('RH', 'RH - Heavy Rain')
					]
		),
		temp_trend=dict(
			choices=[('RR', 'RR - Rising Rapidly (more than 10F)'),
					 ('R', 'R - Rising (2-10F)'),
					 ('S', 'S - Steady'),
					 ('F', 'F - Falling (2-10F)'),
					 ('FR', 'FR - Falling Rapidly (more than 10F)')
			]
		),
		pressure_trend=dict(
			choices=[('RR', 'RR - Rising Rapidly (greater than 2 mb)'),
					 ('R', 'R - Rising (less than 2 mb)'),
					 ('S', 'S - Steady (less than 1 mb in 3 hours'),
					 ('F', 'F - Falling (less than 2 mb)'),
					 ('FR', 'FR - Falling Rapidly (more than 2 mb)')
			]
		),
		wind_direction=dict(
			choices=[('N', 'North'),
					 ('NE', 'North East'),
					 ('E', 'East'),
					 ('SE', 'South East'),
					 ('S', 'South'),
					 ('SW', 'South West'),
					 ('W', 'West'),
					 ('NW', 'North West')
			]
			
		)
	)

class WeatherForView(ModelView):
	form_overrides = dict(condition=SelectField)
	form_args= dict(
		observer=dict(query_factory=observers),
		condition=dict(
			choices=[('GREEN', 'Green - Favorable Conditions'),
					 ('YELLOW', 'Yellow - Favorable but Deteriorating Conditions'),
					 ('RED', 'Red - Above Treeline and Technical Activities Not Recomended')
			]
		)
	)

class TrailView(ModelView):
	column_exclude_list = ('geom')
	
	column_searchable_list = ('name', 'ttype')


#class TrailView(ModelView):
#	can_create = True
#	column_exclude_list = ('geom')
#	form_overrides = dict(location=WTFormsMapField)
#	form_args = dict(
#		geom=dict(geometry_type='MultiLineString', height=500, width=500)
#					)
#	
#	def __init__(self, Trail, session, **kwargs):
#		super(TrailView, self).__init__(Trail, session, **kwargs)
#	
#	def scaffold_form(self):
#		form_class = super(TrailView, self).scaffold_form()
#		form_class.geom = WTFormsMapField()
#		return form_class

class AvalancheInView(ModelView):
    inline_models = (AvalancheInvolved, 
                     InlineFileView(SnowPit), 
                     InlineImageView(Photo),)
    form_overrides = dict(aspect=SelectField, 
                          trigger=SelectField,
                          trigger_add=SelectField,
                          av_problem=SelectField,
                          av_type=SelectField,
                          weak_layer=SelectField)
    form_args = dict(
        aspect= dict(
			choices=[('unknown', 'Unknown'),
			         ('N', 'North'),
					 ('NE', 'North East'),
					 ('E', 'East'),
					 ('SE', 'South East'),
					 ('S', 'South'),
					 ('SW', 'South West'),
					 ('W', 'West'),
					 ('NW', 'North West')
			]
			
		),
		trigger= dict(
    		choices=[('unknown', 'Unknown'),
    		         ('natural', 'Natural'),
    		         ('skier', 'Skier'),
    		         ('snowboarder', 'Snowboarder'),
    		         ('snowmobiler', 'Snowmobiler'),
                     ('snowbike', 'Snow Bike'),
                     ('snowshoer', 'Snowshoer'),
                     ('explosive', 'Explosive'),
                     ('hiker', 'Hiker'),
                     ('other', 'Other')
    		]
		),
		trigger_add= dict(
    		choices=[('unknown', 'Unknown'),
    		         ('intentional', 'Intentionally Triggered'),
                     ('unintentional', 'Unintentionally Triggered'),
                     ('remote', 'Remotely Triggered'),
                     ('cornice', 'Cornice Triggered'),
                     ('sympathetic', 'Sympathetic Release'),
                     ('repeater', 'Repeater')
    		]
		),
		av_problem= dict(
    		choices=[('unknown', 'Unknown'),
    		         ('storm', 'Storm Slab'),
                     ('persistent', 'Persistant Slab'),
                     ('deep', 'Deep Slab'),
                     ('wet', 'Wet Slab'),
                     ('loosedry', 'Loose Dry Snow'),
                     ('loosewet', 'Loose Wet Snow'),
                     ('wind', 'Wind Slab'),
                     ('cornice', 'Cornice'),
                     ('glide', 'Glide')
            ]
		),
		av_type= dict(
    		choices=[('U', 'Unknown'),
    		         ('L', 'Dry Loose'),
                     ('SS', 'Soft Slab'),
                     ('HS', 'Hard Slab'),
                     ('WL', 'Wet Loose'),
                     ('WS', 'Wet Slab'),
                     ('C', 'Cornice Fall'),
                     ('I', 'Ice fall'),
                     ('SF', 'Slush flow'),
                     ('R', 'Roof Avalanche'),
                     
    		]
		),
		weak_layer= dict(
    		choices=[('unknown', 'Unknown'),
    		         ('new', 'New Snow'),
                     ('density', 'Density Change'),
                     ('interface', 'New Snow/Old Snow Interface'),
                     ('facets', 'Facets'),
                     ('depth', 'Depth Hoar'),
                     ('surface', 'Surface Hoar'),
                     ('graupel', 'Graupel'),
                     ('wetgrains', 'Wet Grains'),
                     ('ground', 'Ground Interface')
    		]
		)
    )


class MyAdminIndexView(AdminIndexView):
	
	@expose('/')
	def index(self):
		if not current_user.is_authenticated():
			return redirect(url_for('security.login'))
		return super(MyAdminIndexView, self).index()
	


admin = Admin(name='Baxter Data', index_view=MyAdminIndexView())

admin.add_view(UserView(User, db.session))
admin.add_view(WeatherObView(WeatherOb, db.session, name="Weather Observations", category="Weather"))
admin.add_view(WeatherForView(WeatherFor, db.session, name="Weather Forecasts", category="Weather"))
admin.add_view(ModelView(Trail, db.session, name="Trails", category="Geospatial"))
admin.add_view(ModelView(POI, db.session, name="POI", category="Geospatial"))
admin.add_view(ModelView(AvalanchePath, db.session, name="Avalanche Path", category="Snow"))
admin.add_view(AvalancheInView(AvalancheIn, db.session, name="Avalanche Incident", category="Snow"))
admin.add_view(FileView(SnowPit, db.session, name="Snow Pits", category="Snow"))
admin.add_view(ImageView(Photo, db.session))

#@admin.before_request
#@login_required
#def before_request():
#	pass
#    #if g.user.role != ROLE_ADMIN:
#    #    abort(401)