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
    """
    __tablename__ = 'avalanche_paths'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    description = db.Column(db.Text)
    path = db.Column(Geometry('POLYGON', 926919))


#
#class AvalancheIn(db.Model):
#	"""
#	Avalanche Incident
#	
#	Arguments:
#		id (int): Primary key
#		observer_id (int): Primary foreign key for observer
#		name (string):
#		date (datetime): 
#	"""
#	__tablename__ = 'avalanche_ins'
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
