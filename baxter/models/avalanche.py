from .. import db
from geoalchemy2 import Geometry

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
    



class AvalancheIn(db.Model):
    """
    Avalanche Incident
    
    Arguments:
        id (int): Primary key
        observer_id (int): Primary foreign key for observer
        name (string):
        date (datetime): 
        path_id: 
        path
    """
    __tablename__ = 'avalanche_ins'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    observer = db.relationship('User', backref='avalanche_incidents')
    
    path_id = db.Column(db.Integer, db.ForeignKey('avalanche_paths.id'))
    path = db.relationship('AvalanchePath', backref='incidents')
    
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

    depth = db.Column(db.Float)
    width = db.Column(db.Float)
    vertical = db.Column(db.Float)
    slope_angle = db.Column(db.Float())
    people_caught = db.Column(db.Integer)
    people_carried = db.Column(db.Integer)
    people_buried_part = db.Column(db.Integer)
    people_buried_full = db.Column(db.Integer)
    snow_profile = db.Column(db.Text)
    image = db.Column(db.String(160))
    description = db.Column(db.Text)
    
    crown = db.Column(Geometry('MULTILINESTRING', 926919))
    bed_surface = db.Column(Geometry('MULTIPOLYGON', 926919))
    debris_field = db.Column(Geometry('MULTIPOLYGON', 926919))

class AvalancheInvolved(db.Model):
    """
    People involved in avalanches
    
    Arguments:
        id (int): Primary key
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
    

#
#class AvalancheFor(dn.Model):
#	"""
#	Avalanche Forecast
#	
#	Arguments:
#		
#	"""
#	__tablename__ = "avalanche_forecasts"
#
