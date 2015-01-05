"""
Avalanche related database models.
"""

from .. import db, md

from sqlalchemy import func
from geoalchemy2 import Geometry
from geoalchemy2.shape import to_shape
from flask import Markup
import markdown2


class AvalanchePath(db.Model):
    """
    Avalanche Path

    Arguments:
        id (int): Primary Key
        name (string): Path Name
        description (text): Description of path
        path (Polygon): Avalanche Path
        incidents (List): List of Avalanche Incidents
    """
    __tablename__ = 'avalanche_paths'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    description = db.Column(db.Text)
    path = db.Column(Geometry('POLYGON', 926919))
    aspect = db.Column(db.String(40))

    def center(self):
        """
        Returns a shapely.Point that is the center of the Avalanche Path
        """
        center = to_shape(db.session.query(
            func.ST_Transform(
                func.ST_Centroid(self.path),
                4326
            )
        ).first()[0])
        return center

    def l_center(self):
        """
        Returns a formatted string in a way that
        leaflet likes for a center point
        """
        center = self.center()
        return str(center.y) + ',' + str(center.x)

    def description_md(self):
        """
        Returns a flask Markup object containing the markdown for description
        """
        return Markup(md.convert(self.description))

    def __repr__(self):
        return '%s' % self.name


class AvalancheIn(db.Model):
    """
    Avalanche Incident

    Arguments:
        id (int): Primary key
        observer_id (int): Primary foreign key for observer
        observer (User): User object for observer
        name (string): Name of incident
        path_id (int): Forign key of Avalanche Path where incident occured
        path (AvalanchePath): Object of Avalanche Path where incident occured
        display (bool): Display incident publicly
        observation_date (datetime): Date observer visited incident site
        occurence_date (datetime): Date incident occured
        location (text): Description of incident location
        elevation (int): Elevation of slide path (ft)
        aspect (string): Aspect that the slide occured on
        trigger (string): Start trigger for slide
        trigger_add (string) Additional trigger information
        av_problem (string): Avalanche problem type
        av_type (string): Avalanche type
        weak_layer (string): Weak layer type
        size_relative (float): Slide size relative to path
        size_destructive (float): Destructive force of slide
        depth (float): Depth of displaced snowpack
        width (float): Width of bed surface
        vertical (float): Vertical distance that the slide ran
        slope_angle (float): Steepest Slope Angle
        people_caught (int): Number of people caught by slide
        people_carried (int): Number of people carried by slide
        people_injuried (int): Number of people injured by slide
        people_buried_part (int): Number of people partially burried
        people_buried_full (int): Number of people totally burried
        people_killed (int): Number of people killed by slide
        people_rescuer (int): Number of rescuers involved
        group_activity (str): Activity that group was involved in
        group_travel (str): Group travel method
        snow_profile (text): Description of snowpack
        image (str): DEPRICATED, use photo function
        description (text): Description of slide
        summary (text): Short summary of slide
        crown (MultiLineString): MultiLineString along crown(s)
        bed_surface (MultiPolygon): MultiPolygon of bed surface
        debris_field (MultiPolygon): MultiPolygon of debris field
        problems (AvalancheInProb): List of associated Avalanche Problem objects
        involved (AvalancheInvolved): List of people involved in Avalanches
    """
    __tablename__ = 'avalanche_ins'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    observer = db.relationship('User', backref='avalanche_incidents')

    path_id = db.Column(db.Integer, db.ForeignKey('avalanche_paths.id'))
    path = db.relationship('AvalanchePath', backref='incidents')

    display = db.Column(db.Boolean)

    observation_date = db.Column(db.DateTime)
    occurence_date = db.Column(db.DateTime)
    location = db.Column(db.Text)
    elevation = db.Column(db.Integer)

    aspect = db.Column(db.String(40))
    trigger = db.Column(db.String(40))
    trigger_add = db.Column(db.String(40))
    av_problem = db.Column(db.String(40))
    av_type = db.Column(db.String(40))
    weak_layer = db.Column(db.String(40))
    size_relative = db.Column(db.Float)
    size_desctructive = db.Column(db.Float)

    depth = db.Column(db.Float)
    width = db.Column(db.Float)
    vertical = db.Column(db.Float)
    slope_angle = db.Column(db.Float())

    people_caught = db.Column(db.Integer)
    people_carried = db.Column(db.Integer)
    people_injured = db.Column(db.Integer)
    people_buried_part = db.Column(db.Integer)
    people_buried_full = db.Column(db.Integer)
    people_killed = db.Column(db.Integer)
    people_rescuer = db.Column(db.Integer)

    group_activity = db.Column(db.String(40))
    group_travel = db.Column(db.String(40))

    snow_profile = db.Column(db.Text)
    image = db.Column(db.String(160))
    description = db.Column(db.Text)
    summary = db.Column(db.Text)

    crown = db.Column(Geometry('MULTILINESTRING', 926919))
    bed_surface = db.Column(Geometry('MULTIPOLYGON', 926919))
    debris_field = db.Column(Geometry('MULTIPOLYGON', 926919))

    def center(self):
        """
        Return a shapely.Point that is the center
        of the union of the bed surface and debris field
        """
        center = to_shape(db.session.query(
                func.ST_Transform(
                  func.ST_Centroid(
                    func.ST_Union(self.bed_surface,
                                  self.debris_field
                                  )), 4326)).first()[0])
        return center

    def l_center(self):
        """
        Return a formatted string in a way that
        leaflet likes for a center point
        """
        center = self.center()
        return str(center.y) + ',' + str(center.x)

    def description_md(self):
        """
        Returns a flask Markup object containing the markdown for description
        """
        return Markup(md.convert(self.description))

class AvalancheInvolved(db.Model):
    """
    People involved in avalanches

    Arguments:
        id (int): Primary key
        incident_id (int): Foreign key for associated avalanche incident
        incident (AvalancheIn): Object for associated avalanche incident
        user_id (int): foreign key for associated user
        user (User): Object for associated user
        first (str): First Name
        last (str): Last Name
        phone (str): Phone Number
        email (str): Email Address
        info (Text): More information
        observed (bool): Did they observe the slide?
        group (bool): Were they part of the group that triggered the slide?
        caught (bool): Were they caught by the slide?
        carried (bool): Were they carried by the slide?
        burried (bool): Were they burried by the slide?
        rescuer (bool): Were they a rescuer
        locations (Multipoint): Different locations where the person was
    """
    __tablename__ = 'avalanche_involved'

    id = db.Column(db.Integer, primary_key=True)

    incident_id = db.Column(db.Integer, db.ForeignKey('avalanche_ins.id'))
    incident = db.relationship('AvalancheIn', backref='involved')

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship('User', backref='involved')

    first = db.Column(db.String(40))
    last = db.Column(db.String(40))
    phone = db.Column(db.String(40))
    email = db.Column(db.String(40))
    info = db.Column(db.Text)

    observed = db.Column(db.Boolean)
    group = db.Column(db.Boolean)
    caught = db.Column(db.Boolean)
    carried = db.Column(db.Boolean)
    burried = db.Column(db.Boolean)
    rescuer = db.Column(db.Boolean)

    locations = db.Column(Geometry('MULTIPOINT', 926919))


class AvalancheProb(db.Model):
    """
    Avalanche Problems

    Arguments:
        id (int): Primary key
        name (str): Name of Avalanche Problem
        definition (Text): Long description of Avalanche Problem in markdown
        photo (str): path to photo
    """
    __tablename__ = 'avalanche_problems'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    definition = db.Column(db.Text)
    photo = db.Column(db.String(160))

    def __repr__(self):
        return '%s' % self.name


class AvalancheInProb(db.Model):
    """
    Avalanche Incident and Problem complex connector

    Also known as an `Association Object <http://docs.sqlalchemy.org/en/latest/orm/extensions/associationproxy.html#simplifying-association-objects>`_.

    Arguments:
        id (int): Primary key for AvalancheInProb
        incident_id (int): Foreign Key for associated Avalanche Incident
        incident (AvalancheIn): Object for associated Avalanche Incident
        problem_id (int): Foreign Key for associated Avalanche Problem
        problem (AvalancheProb): Object for associated Avalanche Problem
        importance (str): Rank when multiple problems, lower more important
        aspects (str): Aspects effected by slide
        likelyhood (str): Probability of occurence
        size (str): Size likely
        trend (str): Increasing, steady, or decreasing
        discussion (Text): Discussion of problem
    """
    __tablename__ = 'avalanche_ob_problem'

    id = db.Column(db.Integer, primary_key=True)

    incident_id = db.Column(db.Integer, db.ForeignKey('avalanche_ins.id'))
    incident = db.relationship('AvalancheIn', backref='problems')

    problem_id = db.Column(db.Integer, db.ForeignKey('avalanche_problems.id'))
    problem = db.relationship('AvalancheProb', backref='incidents')

    importance = db.Column(db.Integer)
    aspects = db.Column(db.String(80))
    likelyhood = db.Column(db.String(40))
    size = db.Column(db.String(40))
    trend = db.Column(db.String(40))
    discussion = db.Column(db.Text)



#
#class AvalancheFor(db.Model):
#	"""
#	Avalanche Forecast
#
#	Arguments:
#
#	"""
#	__tablename__ = "avalanche_forecasts"
#
