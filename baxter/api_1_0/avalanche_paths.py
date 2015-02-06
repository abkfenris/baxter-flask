"""
Trail API 1.0
"""

from flask import jsonify, url_for, current_app
import json

from . import api
from .. import db
from .. import cache
from ..models import AvalanchePath


@api.route('/avalanche/path/<int:id>/')
@cache.cached()
def avalanche_path(id):
    """
    return geojson for individual avalanche path
    """
    query = db.session.query(AvalanchePath.name,
            AvalanchePath.id,
            AvalanchePath.aspect,
            AvalanchePath.description,
            AvalanchePath.path.ST_Transform(4326).ST_AsGeoJSON().label('path')
            ).filter_by(id=id)

    path = query[0]

    # make sure the geojson doesn't explode everything
    try:
        geometry = json.loads(path.path)
    except TypeError:
        geometry = {}
    
    current_app.logger.debug('API - Path {0} - ID {1}'.format(path.name, path.id))

    return jsonify({
                'type': 'Feature',
                'properties': {
                    'name': path.name,
                    'id': path.id,
                    'aspect': path.aspect,
                    'description': path.description
                },
                'geometry': geometry
            })


@api.route('/avalanche/path/')
@cache.cached()
def avalanche_paths():
    """
    Geojson for all avalanche paths
    """
    query = db.session.query(AvalanchePath.id,
            AvalanchePath.name,
            AvalanchePath.path.ST_Transform(4326).ST_AsGeoJSON().label('path')
            )

    paths = []
    for path in query:

        # make sure the geojson doesn't explode everything
        try:
            geometry = json.loads(path.path)
        except TypeError:
            geometry = {}

        paths.append({
            'type': 'Feature',
            'properties': {
                'name': path.name,
                'id': path.id,
                'url': url_for('.avalanche_path', id=path.id),
                'html': url_for('main.avalanche_path', id=path.id)
            },
            'geometry': geometry
        })
    
    current_app.logger.debug('API - Path - All')
    
    return jsonify({
        'type': 'FeatureCollection',
        'features': paths
    })
