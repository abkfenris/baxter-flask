from .. import db

from sqlalchemy import func
from geoalchemy2 import Geometry
from geoalchemy2.shape import to_shape


class Trail(db.Model):
    """
    Arguments:
        id (int): Primary Key
        geom (MultiLineString): Multilinestring in NAD 83 UTM Zone 19N for trail route
        use_type (str):
        comments (Text):
        tid (int):
        skitrail (bool): True if it is a ski trail
        name (str): Trail name
        length_mi (float): Length of trail in Miles
        status (str):
        display (bool): Show publicly if true
        pubshare (bool):
        gpsupdate (date): Last time the trail was followed with a GPS
        gpsunit (str): Type of GPS unit used for last update
        gpsuser (str): Who last followed the trail
        bspaid (str):
        tsid (str):
        display_wu (bool):
        display_wn (bool):
        ttype (str): Trail type
        season (str): Is access to trail only allowed during certain seasons
        shape_leng (float):
        tclass (str):
        maintclass (str)
        min_slope (float): Minimum slope of trail
        max_slope (float): Maximum slope of trail
        avg_slope (float): Average slope of trail
        length_ft (float): Length of trail in feet
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

    def center(self):
        """
        Return a shapely.Point that is the center of the trail
        """
        center = to_shape(db.session.query(
            func.ST_Transform(
                func.ST_Centroid(self.geom),
                4326)
            ).first()[0])
        return center

    def l_center(self):
        """
        Return a formatted string in a way that
        leaflet likes for a center point
        """
        center = self.center()
        return str(center.y) + ',' + str(center.x)

    def geojsonitem(self):
        """
        Return a geojson Feature for a trail
        """
        geometry = db.session.query(Trail.geom.ST_Transform(4326).ST_AsGeoJSON().label('geojson')).filter_by(id=self.id).first()[0]
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
        name (str): Name of Point of Interest
        point (Point): Point object in NAD 83 UTM Zone 19N for POI
        bspaid (str):
        poiid (int):
        poi_group (str):
        poi_class (str):
        poi_type (str):
        remark (Text):
        elev_ft (Float): Elevation of Point of Interest
        public_share (bool): Is point publicly visible
        site_capacity (int): How many people can visit site
        facility_id (int):

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
        """
        Return a geojson Feature for Point of Interest
        """
        try:
            geometry = geo.mapping(self.point)
        except AttributeError:
            geometry = None
        return {"type": "Feature",
                "geometry": geometry,
                "properties": {
                    "name": self.name
                    }
                }
