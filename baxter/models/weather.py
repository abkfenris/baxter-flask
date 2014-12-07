from .. import db

class WeatherOb(db.Model):
	"""
	Weather Observation
	
	Arguments:
		id (int): Primary Key
		observer_id (int): Primary foreign key for observer
		observer (object): Observer foreign object
		date (datetime): When the observation was taken
		sky (str): Sky Cover
		precip_type (str): Precipitation Type
		precip_rate (float): Precipitation Rate per hour
		temp_max (float): Maximum 24 hour Temperature
		temp_min (float): Minimum 24 hour Temperature
		temp_present (float): Current Temperature
		temp_trend (string): Temp rising/falling/rate
		pressure_present (float): Current Pressure
		pressure_trend (string): Pressure rising/falling/rate
		humidity (float): Relative Humidity
		wind_speed (float): Wind speed
		wind_direction (str): Wind direction
		wind_gust_max (float): Maximum gust speed
		snow_depth (float): Height of snow depth
		snow_24 (float): 24 hour snow depth
		snow_storm (float): Storm snow depth
		snow_8_temp (float):
		snow_density (float):
		snow_foot_pen
		snow_ram_pen
		snow_surface_form
		snow_surface_size
		snow_blowing_extent
		snow_blowing_direct
		snow_water_equil
		rain_24 (float):
		rain_precip?
		water_new_g?
		water_new_mm
	"""
	__tablename__ = 'weather_observations'
	
	id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
	observer = db.relationship('User', backref='observations')
	
	date = db.Column(db.DateTime)
	
	sky = db.Column(db.String(40))
	
	precip_type = db.Column(db.String(40))
	precip_rate = db.Column(db.String(40))
	
	temp_max = db.Column(db.Float)
	temp_min = db.Column(db.Float)
	temp_present = db.Column(db.Float)
	temp_trend = db.Column(db.String(40))
	
	pressure_present = db.Column(db.Float)
	pressure_trend = db.Column(db.String(40))
	
	humidity = db.Column(db.Float)
	
	wind_speed = db.Column(db.Float)
	wind_direction = db.Column(db.String(40))
	wind_gust_max = db.Column(db.Float)
	
	rain_24 = db.Column(db.Float)
	
	snow_depth = db.Column(db.Float)
	snow_24 = db.Column(db.Float)
	snow_storm = db.Column(db.Float)
	snow_8_temp = db.Column(db.Float)
	snow_density = db.Column(db.Float)
	
	snow_foot_pen = db.Column(db.Float)
	snow_ram_pen = db.Column(db.Float)
	
	snow_surface_form = db.Column(db.String(80))
	snow_surface_size = db.Column(db.Float)
	snow_blowing_extent = db.Column(db.String(40))
	snow_water_equil = db.Column(db.Float)
	


class WeatherFor(db.Model):
	"""
	Weather Forecast
	
	Arguments:
		id (int): Primay Key
		observer_id (int): Forecaster/Observer foreign id
		oberver: Forecaster/Observer object
		Condition (list): Mountain Condition
		for_temp_high (int): High temperature
		for_temp_low (int): Low temperature
		trail_comment (text): Trail condition information
		for_today (text): Today's forecast
		for_tomorrow (text): Tomorrow's forecast
		for_long (text): Long term forecast
		body (text): Forecasters's comments
		
	"""
	__tablename__ = 'weather_forecasts'
	
	id = db.Column(db.Integer, primary_key=True)
	
	user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
	observer = db.relationship('User', backref='weather_forecasts')
	
	condition = db.Column(db.String(40))

	for_temp_high = db.Column(db.Integer)
	for_temp_low = db.Column(db.Integer)
	
	trail_comment = db.Column(db.Text)
	
	for_today = db.Column(db.Text)
	for_tomorrow = db.Column(db.Text)
	for_long = db.Column(db.Text)
	
	body = db.Column(db.Text)