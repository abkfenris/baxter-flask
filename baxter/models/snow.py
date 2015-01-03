from .. import db
from geoalchemy2 import Geometry


class SnowPit(db.Model):
    """
    Snowpit

    Arguments:
        id (int): Primary key
        name (unicode): Descriptive name of snow pit data
        path (unicode): filename
        location (Point): Point in NAD 83 UTM Zone 19N for snow pit
        description (Text): Description of snow pit
    """
    __tablename__ = 'snowpits'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode(64))
    path = db.Column(db.Unicode(128))
    location = db.Column(Geometry("POINT", 926919))
    description = db.Column(db.Text)

    incident_id = db.Column(db.Integer, db.ForeignKey('avalanche_ins.id'))
    incident = db.relationship('AvalancheIn', backref='snowpit')

    def __unicode__(self):
        return self.name
