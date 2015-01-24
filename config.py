import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = (os.environ.get('SECRET_KEY') or
                  'vwk67hNn6Uxd[C3B^9o=3X*G3oUK4yzYiTrwRrA;)zm[9]8]&p')
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    MAPBOX_MAP_ID = os.environ.get('MAPBOX_MAP_ID')
    SECURITY_POST_LOGIN_VIEW = 'admin/'

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/baxter'
    CACHE_TYPE = 'simple'
    CACHE_DEFAULT_TIMEOUT = 50


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/baxter_testing'
    CACHE_TYPE = 'simple'
    CACHE_DEFAULT_TIMEOUT = 50


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = (os.environ.get('BAXTER_DB') or
                               'postgresql://localhost/baxter')
    CACHE_TYPE = 'simple'
    CACHE_DEFAULT_TIMEOUT = 120
    CACHE_KEY_PREFIX = 'bc_'
    CACHE_REDIS_HOST = os.environ.get('BAXTER_REDIS_HOST')
    CACHE_REDIS_PASSWORD = os.environ.get('BAXTER_REDIS_PASSWORD')
    SECURITY_PASSWORD_HASH = 'bcrypt'
    SECURITY_PASSWORD_SALT = (os.environ.get('SECRET_KEY') or
                  'vwk67hNn6Uxd[C3B^9o=3X*G3oUK4yzYiTrwRrA;)zm[9]8]&p')


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}
