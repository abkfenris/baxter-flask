"""
The main public routes to view the site
"""

from flask import (render_template,
                   Response,
                   make_response,
                   url_for,
                   current_app)

from . import main
from .. import db
from ..models import User, WeatherOb, WeatherFor


@main.route('/')
def index():
    return render_template('index.html')

@main.route('/trails/')
def trails():
    return render_template('trails.html')
