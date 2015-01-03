"""
Version 1.0 of the API
"""

from flask import Blueprint  # , jsonify, url_for

# from .. import db
# from ..models import Trail

api = Blueprint('api', __name__)

from . import trails, avalanche_incidents
