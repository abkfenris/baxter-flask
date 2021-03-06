"""
The avalanche incident routes to view the site
"""

from flask import (render_template,
                   Response,
                   make_response,
                   url_for,
                   current_app)

from . import main
from .. import db
from ..mappers import (aspects,
                       triggers,
                       triggers_add,
                       av_problems,
                       av_types,
                       weak_layers,
                       avalanche_relative,
                       avalanche_destructive)
from ..models import AvalancheIn


@main.route('/avalanche/incident/')
def avalanche_incidents():
    """
    Show all incidents
    """
    query = db.session.query(AvalancheIn.id,
                             AvalancheIn.name,
                             AvalancheIn.occurence_date,
                             AvalancheIn.location
                             ).order_by(AvalancheIn.occurence_date.desc())
    incidents = query
    current_app.logger.debug('Avalanche incident list')
    return render_template('avalanche/incidents.html', incidents=incidents)


@main.route('/avalanche/incident/<int:id>')
def avalanche_incident(id):
    """
    Show a single incident
    """
    incident = AvalancheIn.query.get_or_404(id)
    try:
        relative = avalanche_relative[str(incident.size_relative)]
    except KeyError:
        relative = 'Unknown'
    try:
        destructive = avalanche_destructive[str(incident.size_desctructive)]
    except KeyError:
        destructive = 'Unknown'
    current_app.logger.debug('Avalanche incident {0} - ID {1}'.format(incident.name, incident.id))
    return render_template('avalanche/incident.html',
                           incident=incident,
                           aspects=aspects,
                           triggers=triggers,
                           triggers_add=triggers_add,
                           av_problems=av_problems,
                           av_types=av_types,
                           weak_layers=weak_layers,
                           relative=relative,
                           destructive=destructive)
