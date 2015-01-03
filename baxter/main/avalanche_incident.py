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
                       weak_layers)
from ..models import AvalancheIn


@main.route('/avalanche/incident/')
def incidents():
    """
    Show all incidents
    """
    query = db.session.query(AvalancheIn.id,
                             AvalancheIn.name,
                             AvalancheIn.occurence_date,
                             AvalancheIn.location
                             ).order_by(AvalancheIn.occurence_date.desc())
    incidents = query
    return render_template('avalanche-incidents.html', incidents=incidents)


@main.route('/avalanche/incident/<int:id>')
def incident(id):
    """
    Show a single incident
    """
    incident = AvalancheIn.query.get_or_404(id)
    return render_template('avalanche-incident.html',
                           incident=incident,
                           aspects=aspects,
                           triggers=triggers,
                           triggers_add=triggers_add,
                           av_problems=av_problems,
                           av_types=av_types,
                           weak_layers=weak_layers)
