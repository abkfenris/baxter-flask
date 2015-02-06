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
    """
    Index page for site.
    """
    current_app.logger.debug('Index page')
    return render_template('index.html')
