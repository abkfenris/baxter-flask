"""
Trail API 1.0
"""

from flask import jsonify, url_for
import json

from . import api
from .. import db
from .. import cache
from ..models import AvalancheIn

@api.route('/avalanche/incident/<int:id>/')
def incident(id):
    """
    return geojson for individual avalanche incident
    """
    query = db.session.query(AvalancheIn.name,
            AvalancheIn.id,
            AvalancheIn.crown.ST_Transform(4326).ST_AsGeoJSON().label('crown'),
            AvalancheIn.bed_surface.ST_Transform(4326).ST_AsGeoJSON().label('bed_surface'),
            AvalancheIn.debris_field.ST_Transform(4326).ST_AsGeoJSON().label('debris_field'),
            ).filter_by(id=id)

    incident = query[0]
    return jsonify({
        'type': 'Feature',
        'properties': {
            'name': incident.name,
            'id': incident.id
        },
        'geometry': {
            'type': 'GeometryCollection',
            'geometries': [
                json.loads(incident.crown),
                json.loads(incident.bed_surface),
                json.loads(incident.debris_field)
            ]
        }
    })
