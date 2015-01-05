"""
Admin interface, sets up admin views
"""
import os
import os.path as op

from flask import url_for, redirect
from flask.ext.admin import Admin, AdminIndexView, expose
from flask.ext.admin.base import MenuLink
from flask.ext.admin.contrib.geoa import ModelView as _ModelView
# from flask.ext.admin.form import rules
from wtforms.fields import SelectField
from sqlalchemy.event import listens_for
from flask.ext.admin.form import (FileUploadField,
                                  ImageUploadField,
                                  thumbgen_filename)
from flask.ext.admin.model import InlineFormAdmin
from flask.ext.security import (roles_required,
                                roles_accepted,
                                current_user,
                                login_required)
# from jinja2 import Markup

from .. import db
from ..models import (User,
                      WeatherOb, WeatherFor,
                      Trail, POI,
                      AvalanchePath, AvalancheIn,
                      AvalancheInvolved, AvalancheProb,
                      AvalancheInProb,
                      Photo, SnowPit)
from ..mappers import (aspects,
                       directions,
                       triggers,
                       triggers_add,
                       av_problems,
                       av_types,
                       weak_layers,
                       conditions,
                       sky_covers,
                       precip_types,
                       precip_rates,
                       temp_trends,
                       pressure_trends,
                       avalanche_relative,
                       avalanche_destructive
                       )

# File path
file_path = op.join(op.dirname(__file__), 'files')
try:
    os.makedirs(file_path)
except OSError:
    pass

pit_path = op.join(op.dirname(op.dirname(__file__)), 'static', 'uploaded' ,'pits')
pit_static_path = '/static/uploaded/pits/'
try:
    os.makedirs(pit_path)
except OSError:
    pass

photo_path = op.join(op.dirname(op.dirname(__file__)), 'static', 'uploaded', 'photos')
photo_static_path = '/static/uploaded/photos/'
try:
    os.makedirs(photo_path)
except OSError:
    pass

# height and width for map editing fields
h_w = {'data-height': 400, 'data-width': 600}

# Delete Hook for SnowPit, delete file if model is deleted
@listens_for(SnowPit, 'after_delete')
def del_snowpit(mapper, connection, target):
    if target.path:
        try:
            os.remove(op.join(pit_path, target.path))
        except OSError:
            # Don't care as it doesn't exist
            pass


@listens_for(Photo, 'after_delete')
def del_photo(mapper, connection, target):
    if target.path:
        # Delete Image
        try:
            os.remove(op.join(photo_path, target.path))
        except OSError:
            pass

        # Delete the thumbnail
        try:
            os.remove(op.join(photo_path, thumbgen_filename(target.path)))
        except OSError:
            pass


class ModelView(_ModelView):
    def is_accessible(self):
        return current_user.is_authenticated()

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('security.login'))


class FileView(ModelView):
    form_overrides = {'path': FileUploadField}
    form_args = {'path': {'label': 'File',
                          'base_path': pit_path}}
    column_formatters = {'path': lambda v, c, m, p: pit_static_path + m.path}
    column_list = ('name', 'path', 'location', 'description')

class InlineAvalancheInProb(InlineFormAdmin):
    pass


class InlineFileView(InlineFormAdmin):
    form_overrides = {'path': FileUploadField}
    form_args = {'path': {'label': 'File',
                          'base_path': pit_path}}
    form_widget_args = {'location': h_w}


class ImageView(ModelView):
    form_extra_fields = {
        'path': ImageUploadField('Photo',
                                 base_path=photo_path,
                                 url_relative_path='../static/uploaded/photos/',
                                 thumbnail_size=(100, 100, True))
    }
    # Make the full linkable photo path show up on the list view
    column_formatters = {'path': lambda v, c, m, p: photo_static_path + m.path}
    column_list = ('name', 'path', 'description', 'location')


class InlineImageView(InlineFormAdmin):
    form_overrides = {'path': ImageUploadField}
    form_args = {'path': {'label': 'Photo',
                          'base_path': photo_path}}
    form_widget_args = {'location': h_w}


class InlineInvolvedView(InlineFormAdmin):
    form_widget_args = {'locations': h_w}
    #form_rules = ['user',
    #    rules.Header('Test Header'),
    #    rules.FieldSet(('first', 'last'), header='Name'),
    #    rules.FieldSet(('phone','email')),
    #    'info',
    #    rules.FieldSet((rules.HTML('<div class="row">'),
    #                    'observed',
    #                    'group',
    #                    'caught',
    #                    'carried',
    #                    'burried',
    #                    'rescuer',
    #                    rules.HTML('</div>'))),
    #    'locations'
    #] # Trying to format the inline form smaller


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
    form_args = {'observer': {'query_factory': observers},
                 'sky': {'choices': sky_covers.items()},
                 'precip_type': {'choices': precip_types.items()},
                 'precip_rate': {'choices': precip_rates.items()},
                 'temp_trend': {'choices': temp_trends.items()},
                 'pressure_trend': {'choices': pressure_trends.items()},
                 'wind_direction': {'choices': directions.items()}
                 }


class WeatherForView(ModelView):
    form_overrides = dict(condition=SelectField)
    form_args = {
        'observer': {'query_factory': observers},
        'condition': {'choices': conditions.items()}
    }


class TrailView(ModelView):
    column_list = ('name',
                   'display',
                   'pubshare',
                   'ttype',
                   'tclass',
                   'season',
                   'geom')
    column_searchable_list = ('name', 'ttype')


class AvalancheProbView(ModelView):
    pass


#class TrailView(ModelView):
#    can_create = True
#    column_exclude_list = ('geom')
#    form_overrides = dict(location=WTFormsMapField)
#    form_args = dict(
#        geom=dict(geometry_type='MultiLineString', height=500, width=500)
#                    )
#
#    def __init__(self, Trail, session, **kwargs):
#        super(TrailView, self).__init__(Trail, session, **kwargs)
#
#    def scaffold_form(self):
#        form_class = super(TrailView, self).scaffold_form()
#        form_class.geom = WTFormsMapField()
#        return form_class

class AvalancheInView(ModelView):
    inline_models = (InlineInvolvedView(AvalancheInvolved),
                     InlineFileView(SnowPit),
                     InlineImageView(Photo),
                     InlineAvalancheInProb(AvalancheInProb))
    form_overrides = dict(aspect=SelectField,
                          trigger=SelectField,
                          trigger_add=SelectField,
                          av_problem=SelectField,
                          av_type=SelectField,
                          weak_layer=SelectField,
                          size_relative=SelectField,
                          size_desctructive=SelectField)
    form_args = {'aspect': {'choices': aspects.items()},
                 'trigger': {'choices': triggers.items()},
                 'trigger_add': {'choices': triggers_add.items()},
                 'av_problem': {'choices': av_problems.items()},
                 'av_type': {'choices': av_types.items()},
                 'weak_layer': {'choices': weak_layers.items()},
                 'size_relative': {'choices': avalanche_relative.items()},
                 'size_desctructive': {'choices': avalanche_destructive.items()},
                 'observer': {'query_factory':observers}
                 }
    form_widget_args = {'crown': h_w,
                        'bed_surface': h_w,
                        'debris_field': h_w,
                        'description': {
                            'rows': 15
                        }}
    column_list = ('name', 'occurence_date', 'depth', 'width', 'vertical', 'aspect', 'observer', 'bed_surface', 'debris_field')


class MyAdminIndexView(AdminIndexView):

    @expose('/')
    def index(self):
        if not current_user.is_authenticated():
            return redirect(url_for('security.login'))
        return super(MyAdminIndexView, self).index()


class AuthenticatedMenuLink(MenuLink):
    def is_accessible(self):
        return current_user.is_authenticated()


admin = Admin(name='Baxter Data',
              index_view=MyAdminIndexView(),
              template_mode='bootstrap3')

admin.add_view(UserView(User, db.session,
                        name="Users",
                        endpoint='admin.users',
                        url='user'))
admin.add_view(WeatherObView(WeatherOb, db.session,
                             name="Weather Observations",
                             category="Weather",
                             endpoint='admin.weatherob',
                             url='weatherob'))
admin.add_view(WeatherForView(WeatherFor, db.session,
                              name="Weather Forecasts",
                              category="Weather",
                              endpoint='admin.weatherfor',
                              url='weatherfor'))
admin.add_view(TrailView(Trail, db.session,
                         name="Trails",
                         category="Geospatial",
                         endpoint='admin.trail',
                         url='trail'))
admin.add_view(ModelView(POI, db.session,
                         name="POI",
                         category="Geospatial",
                         endpoint='admin.poi',
                         url='poi'))
admin.add_view(ModelView(AvalanchePath, db.session,
                         name="Avalanche Path",
                         category="Snow",
                         endpoint='admin.avalanchepath',
                         url='avalanchepath'))
admin.add_view(AvalancheInView(AvalancheIn, db.session,
                               name="Avalanche Incident",
                               category="Snow",
                               endpoint='admin.avalanchein',
                               url='avalanchein'))
admin.add_view(AvalancheProbView(AvalancheProb, db.session,
                                 name="Avalanche Problems",
                                 category="Snow",
                                 endpoint='admin.avalancheprob',
                                 url='avalancheprob'))
admin.add_view(FileView(SnowPit, db.session,
                        name="Snow Pits",
                        category="Snow",
                        endpoint='admin.snowpit',
                        url='snowpit'))
admin.add_view(ImageView(Photo, db.session,
                         name="Photos",
                         endpoint='admin.photo',
                         url='photo'))
admin.add_link(AuthenticatedMenuLink(name='Logout',
                                     endpoint='security.logout'))
