import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'vwk67hNn6Uxd[C3B^9o=3X*G3oUK4yzYiTrwRrA;)zm[9]8]&p'
	SQLALCHEMY_COMMIT_ON_TEARDOWN = True
	MAPBOX_MAP_ID = os.environ.get('MAPBOX_MAP_ID')
	
	@staticmethod
	def init_app(app):
		pass

class DevelopmentConfig(Config):
	DEBUG = True
	SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/baxter'

class TestingConfig(Config):
	TESTING = True
	SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/baxter_testing'

class ProductionConfig(Config):
	SECURITY_PASSWORD_HASH = 'bcrypt'

config = {
	'development': DevelopmentConfig,
	'testing': TestingConfig,
	'production': ProductionConfig,
	
	'default': DevelopmentConfig
}