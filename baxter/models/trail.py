from .. import db
from geoalchemy2 import Geometry

class Trail(db.Model):
	"""
	Arguments:
		
	"""
	__tablename__ = 'trails'
	
	id = db.Column(db.Integer, primary_key=True)
	geom = db.Column(Geometry('MULTILINESTRING', 926919))
	use_type = db.Column(db.String(40))
	comments = db.Text()
	tid = db.Column(db.Integer)
	skitrail = db.Column(db.Boolean)
	name = db.Column(db.String(120))
	length_mi = db.Column(db.Float)
	status = db.Column(db.String(40))
	display = db.Column(db.Boolean)
	pubshare = db.Column(db.Boolean)
	gpsupdate = db.Column(db.Date)
	gpsunit = db.Column(db.String(40))
	gpsuser = db.Column(db.String(40))
	bspaid = db.Column(db.String(40))
	tsid = db.Column(db.String(40))
	display_wu = db.Column(db.Boolean)
	display_wn = db.Column(db.Boolean)
	ttype = db.Column(db.String(40))
	season = db.Column(db.String(40))
	shape_leng = db.Column(db.Float)
	tclass = db.Column(db.String(40))
	maintclass = db.Column(db.String(40))
	slength = db.Column(db.Float)
	min_slope = db.Column(db.Float)
	max_slope = db.Column(db.Float)
	avg_slope = db.Column(db.Float)
	length_ft = db.Column(db.Float)
	
	def geojsonitem(self):
		try:
			geometry = geo.mapping(self.geom)
		except AttributeError:
			geometry = None
		return {"type": "Feature",
				"geometry": geometry,
				"properties": {"name": self.name,
							   "use_type": self.use_type,
							   "comments": self.comments,
							   "tid": self.tid,
							   "skitrail": self.skitrail,
							   "length_mi": self.length_mi,
							   "status": self.status,
							   "display": self.display,
							   "pubshare": self.pubshare,
							   "gpsupdate": self.gpsupdate,
							   "gpsunit": self.gpsunit,
							   "gpsuser": self.gpsuser,
							   "bspaid": self.bspaid,
							   "tsid": self.tsid,
							   "display_wu": self.display_wu,
							   "display_wn": self.display_wn,
							   "type": self.ttype,
							   "season": self.season,
							   "shape_leng": self.shape_leng,
							   "class": self.tclass,
							   "maintclass": self.maintclass,
							   "slength": self.slength,
							   "min_slope": self.min_slope,
							   "max_slope": self.max_slope,
							   "avg_slope": self.avg_slope,
							   "length_ft": self.length_ft
							   }
				}
	

class POI(db.Model):
    """
    Points of Interest
    
    Arguments:
        id (int): Primary Key
        
    """
    __tablename__ = 'points_of_interests'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40))    
    point = db.Column(Geometry("POINT", 926919))
    bspaid = db.Column(db.String(40))
    poiid = db.Column(db.Integer)
    poi_group = db.Column(db.String(40))
    poi_class = db.Column(db.String(40))
    poi_type = db.Column(db.String(40))
    remark = db.Column(db.Text)
    elev_ft = db.Column(db.Float)
    public_share = db.Column(db.Boolean)
    site_capacity = db.Column(db.Integer)
    facility_id = db.Column(db.Integer)
    
    
    def geojsonitem(self):
        try:
        	geometry = geo.mapping(self.point)
        except AttributeError:
        	geometry = None
        return {"type": "Feature",
        		"geometry": geometry,
        		"properties": {
        			"name" : self.name
        			}
        		}