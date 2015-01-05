"""
Trail API 1.0
"""

from flask import jsonify, url_for
import json

from . import api
from .. import db
from .. import cache
from ..models import Trail

@api.route('/trail/<int:id>/')
@cache.cached()
def trail(id):
    """
    Show individual trail *id*
    """
    query = db.session.query(Trail.name,
            Trail.id,
            Trail.geom.ST_Transform(4326).ST_AsGeoJSON().label('geojson')
            ).filter_by(id=id,display=True)
    trail = query[0]

    # keep geojson from exploding everything if it doesn't exist
    try:
        geojson = json.loads(trail.geojson)
    except TypeError:
        geojson = {}

    return jsonify({
        'type': 'Feature',
        'properties': {
            'name': trail.name,
            'id': trail.id
        },
        'geometry': geojson
    })


@api.route('/trail/')
@cache.cached()
def list_trails():
    """
    Show all trails
    """
    query = db.session.query(Trail.name,
            Trail.id,
            Trail.geom.ST_Transform(4326).ST_AsGeoJSON().label('geojson')
            ).filter_by(display=True)

    trails = []
    for trail in query:

        # make it so that a lack of geojson doesn't explode everything
        try:
            geojson = json.loads(trail.geojson)
        except TypeError:
            geojson = {}

        trails.append({
            'type': 'Feature',
            'properties': {
                'name': trail.name,
                'id': trail.id,
                'url': url_for('.trail', id=trail.id),
                'html': url_for('main.trail', id=trail.id)
            },
            'geometry': geojson
        })

    return jsonify({
        'type': 'FeatureCollection',
        'features': trails
    })
