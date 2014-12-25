"""
Trail API 1.0
"""

from flask import jsonify, url_for
import json

from . import api
from .. import db
from .. import cache
from ..models import Trail

@api.route('/trails/<id>')
def trail(id):
    query = db.session.query(Trail.name,
            Trail.id,
            Trail.geom.ST_Transform(4326).ST_AsGeoJSON().label('geojson')
            ).filter_by(id=id,display=True)

    return jsonify({
        'type': 'Feature',
        'properties': {
            'name': query[0].name,
            'id': query[0].id
        },
        'geometry': json.loads(query[0].geojson)
    })


@api.route('/trails/')
@cache.cached()
def list_trails():
    query = db.session.query(Trail.name,
            Trail.id,
            Trail.geom.ST_Transform(4326).ST_AsGeoJSON().label('geojson')
            ).filter_by(display=True)

    trails = []
    for trail in query:
        trails.append({
            'type': 'Feature',
            'properties': {
                'name': trail.name,
                'id': trail.id,
                'url': url_for('.trail', id=trail.id)
            },
            'geometry': json.loads(trail.geojson)
        })
    return jsonify({
        'type': 'FeatureCollection',
        'features': trails
    })
