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
            AvalancheIn.observation_date,
            AvalancheIn.occurence_date,
            AvalancheIn.location,
            AvalancheIn.elevation,
            AvalancheIn.aspect,
            AvalancheIn.trigger,
            AvalancheIn.trigger_add,
            AvalancheIn.av_problem,
            AvalancheIn.av_type,
            AvalancheIn.weak_layer,
            AvalancheIn.depth,
            AvalancheIn.width,
            AvalancheIn.vertical,
            AvalancheIn.slope_angle,
            AvalancheIn.description,
            AvalancheIn.crown.ST_Transform(4326).ST_AsGeoJSON().label('crown'),
            AvalancheIn.bed_surface.ST_Transform(4326).ST_AsGeoJSON().label('bed_surface'),
            AvalancheIn.debris_field.ST_Transform(4326).ST_AsGeoJSON().label('debris_field'),
            AvalancheIn.bed_surface.ST_Union(AvalancheIn.debris_field).ST_Transform(4326).ST_AsGeoJSON().label('geojson')
            ).filter_by(id=id)

    incident = query[0]
    return jsonify({
        'type': 'FeatureCollection',
        'features': [
            {
                'type': 'Feature',
                'properties': {
                    'structure': 'crown'
                },
                'geometry': json.loads(incident.crown)
            },
            {
                'type': 'Feature',
                'properties': {
                    'structure': 'bed surface'
                },
                'geometry': json.loads(incident.bed_surface)
            },
            {
                'type': 'Feature',
                'properties': {
                    'structure': 'debris field'
                },
                'geometry': json.loads(incident.debris_field)
            },
            {
                'type': 'Feature',
                'properties': {
                    'name': incident.name,
                    'id': incident.id,
                    'observation date': incident.observation_date,
                    'occurence date': incident.occurence_date,
                    'location': incident.location,
                    'elevation': incident.elevation,
                    'aspect': incident.aspect,
                    'trigger': incident.trigger,
                    'trigger info': incident.trigger_add,
                    'avalanche problem': incident.av_problem,
                    'avalanche type': incident.av_type,
                    'weak layer': incident.weak_layer,
                    'depth': incident.depth,
                    'width': incident.width,
                    'vertical': incident.vertical,
                    'slope angle': incident.slope_angle,
                    'description': incident.description
                },
                'geometry': json.loads(incident.geojson)
            }
        ]
    })


@api.route('/avalanche/incident/<int:id>/parts')
def incident_parts(id):
    """
    return geojson for individual avalanche incident
    """
    query = db.session.query(AvalancheIn.name,
            AvalancheIn.id,
            AvalancheIn.crown.ST_Transform(4326).ST_AsGeoJSON().label('crown'),
            AvalancheIn.bed_surface.ST_Transform(4326).ST_AsGeoJSON().label('bed_surface'),
            AvalancheIn.debris_field.ST_Transform(4326).ST_AsGeoJSON().label('debris_field'),
            AvalancheIn.bed_surface.ST_Union(AvalancheIn.debris_field).ST_Transform(4326).ST_AsGeoJSON().label('geojson')
            ).filter_by(id=id)

    incident = query[0]
    return jsonify({
        'type': 'FeatureCollection',
        'features': [
            {
                'type': 'Feature',
                'properties': {
                    'structure': 'crown'
                },
                'geometry': json.loads(incident.crown)
            },
            {
                'type': 'Feature',
                'properties': {
                    'structure': 'bed surface'
                },
                'geometry': json.loads(incident.bed_surface)
            },
            {
                'type': 'Feature',
                'properties': {
                    'structure': 'debris field'
                },
                'geometry': json.loads(incident.debris_field)
            }
        ]
    })


@api.route('/avalanche/incident/')
def incidents():
    """
    Geojson for all avalanche incidents
    """
    query = db.session.query(AvalancheIn.id,
            AvalancheIn.occurence_date,
            AvalancheIn.name,
            AvalancheIn.bed_surface.ST_Union(AvalancheIn.debris_field).ST_Transform(4326).ST_AsGeoJSON().label('geojson')
            )
    incidents = []
    for incident in query:
        incidents.append({
            'type': 'Feature',
            'properties': {
                'name': incident.name,
                'id': incident.id,
                'occurance date': incident.occurence_date,
                'url': url_for('.incident', id=incident.id)
            },
            'geometry': json.loads(incident.geojson)
        })
    return jsonify({
        'type': 'FeatureCollection',
        'features': incidents
    })
