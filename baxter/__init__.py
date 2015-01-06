#!/usr/bin/python

"""
App builder. Can be imported and used to start the site
"""

from flask import Flask
from flask.ext.bootstrap import Bootstrap
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.security import Security
from flask.ext.cache import Cache
from config import config
from flask_debugtoolbar import DebugToolbarExtension
import markdown2

bootstrap = Bootstrap()
db = SQLAlchemy()
security = Security()
toolbar = DebugToolbarExtension()
cache = Cache()

md = markdown2.Markdown(extras={'html-classes': {'img': 'img-responsive'}})

from .models import user_datastore

def create_db_and_roles():
    db.create_all()
    from .models import Role
    contrib = Role(name='contributor', description='Contributor Role')
    user = Role(name='user', description='User Role')
    admin = Role(name='admin', description='Admin Role')
    db.session.add(contrib)
    db.session.add(user)
    db.session.add(admin)
    db.session.commit()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    bootstrap.init_app(app)
    db.init_app(app)
    security.init_app(app, user_datastore)
    cache.init_app(app)

    toolbar.init_app(app)

    from .main import main
    app.register_blueprint(main)

    from .admin import admin
    admin.init_app(app)

    from . api_1_0 import api as api_1_0_blueprint
    app.register_blueprint(api_1_0_blueprint, url_prefix='/api/1.0')

    return app
