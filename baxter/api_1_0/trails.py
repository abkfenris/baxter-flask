"""
Trail API 1.0
"""

from flask import jsonify, url_for
import json

from . import api
from .. import db
from ..models import Trail

@api.route('/trails/<id>')
def trail(id):
    query = db.session.query(Trail.name,
            Trail.geom.ST_Transform(4326).ST_AsGeoJSON().label('geojson')
            ).filter_by(id=id)

    return jsonify({
        'type': 'Feature',
        'properties': {
            'name': query[0].name,
        },
        'geometry': json.loads(query[0].geojson)
    })


@api.route('/trails/')
def list_trails():
    query = db.session.query(Trail.name,
            Trail.id,
            Trail.geom.ST_Transform(4326).ST_AsGeoJSON().label('geojson')
            )

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
