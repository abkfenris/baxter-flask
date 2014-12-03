"""
Admin interface, sets up admin views
"""

from flask.ext.admin import Admin
from flask.ext.admin.contrib.sqla import ModelView
from wtforms.fields import SelectField

from . import db
from models import User, WeatherOb, WeatherFor

class UserView(ModelView):
	pass


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



admin = Admin(name='Baxter Data')

admin.add_view(UserView(User, db.session))
admin.add_view(WeatherObView(WeatherOb, db.session))
admin.add_view(WeatherForView(WeatherFor, db.session))
