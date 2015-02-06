"""
The trail routes to view the site
"""

from flask import (render_template,
                   Response,
                   make_response,
                   url_for,
                   current_app)

from . import main
from .. import db
from ..models import Trail


@main.route('/trails/')
def trails():
    """
    Show all trails
    """
    trails = db.session.query(Trail.name,
                             Trail.id,
                             Trail.season,
                             Trail.skitrail,
                             Trail.length_mi
                             ).filter_by(display=True, tclass='ACTIVE').order_by(Trail.name.asc())
    current_app.logger.debug('Trail list')
    return render_template('trails.html', trails=trails)


@main.route('/trails/<id>/')
def trail(id):
    """
    Show a single trail
    """
    trail = Trail.query.get_or_404(id)
    current_app.logger.debug('Trail {0} - ID {1}'.format(trail.name, trail.id))
    return render_template('trail.html', trail=trail)
