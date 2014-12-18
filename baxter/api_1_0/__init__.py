"""
Version 1.0 of the API
"""

from flask import Blueprint, jsonify, url_for

from .. import db
from ..models import Trail
import json

api = Blueprint('api', __name__)

@api.route('/<id>')
def trail(id):
	query = db.session.query(Trail.name, Trail.geom.ST_AsGeoJSON().label('geojson')).filter_by(id=id)
	
	return jsonify({
		'type': 'Feature',
		'properties': {
			'name':query[0].name,
		},
		'geometry': json.loads(query[0].geojson)
	})

@api.route('/')
def index():
	query = db.session.query(Trail.name, Trail.id, Trail.geom.ST_Transform(4326).ST_AsGeoJSON().label('geojson'))
	
	trails = []
	for trail in query:
		trails.append({
			'type': 'Feature',
			'properties': {
				'name': trail.name,
				'url': url_for('.trail', id=trail.id)
			},
			'geometry': json.loads(trail.geojson)
		})
	return jsonify({
		'type': 'FeatureCollection',
		'features': trails
	})