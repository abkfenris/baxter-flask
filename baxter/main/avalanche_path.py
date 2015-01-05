"""
The Avalanche Path routes to view the site
"""

from flask import (render_template,
                   Response,
                   make_response,
                   url_for,
                   current_app)

from . import main
from .. import db
from ..models import AvalanchePath


@main.route('/avalanche/path/')
def avalanche_paths():
    """
    Show all avalanche paths
    """
    paths = db.session.query(AvalanchePath.name,
                             AvalanchePath.id,
                             ).order_by(AvalanchePath.name.asc())
    return render_template('avalanche/paths.html', paths=paths)


@main.route('/avalanche/path/<id>/')
def avalanche_path(id):
    """
    Show a single trail
    """
    path = AvalanchePath.query.get_or_404(id)
    return render_template('avalanche/path.html', path=path)
