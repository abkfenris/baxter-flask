from .. import db
from geoalchemy2 import Geometry


avalanche_ins_snowpit = db.Table('avalanche_ins_snowpit',
        db.Column('avalanche_ins_id', db.Integer, db.ForeignKey('avalanche_ins.id')),
        db.Column('snowpit_id', db.Integer, db.ForeignKey('snowpits.id')),
)


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

    incident = db.relationship('AvalancheIn', secondary=avalanche_ins_snowpit,
            backref=db.backref('snowpits', lazy='dynamic'))

    def __unicode__(self):
        return str(self.name)
