from .. import db
from geoalchemy2 import Geometry


#AvalancheIn_Photo = db.Table('avalanche_ins_photo',
#        db.Column('avalanche_ins_id', db.Integer, db.ForeignKey('avalanche_ins.id')),
#        db.Column('photo_id', db.Integer, db.ForeignKey('photo.id')),
#)


class Photo(db.Model):
    """
    Photo

    Arguments:
        id (int): Primary Key for Photos
        name (Unicode): filename
        path (Unicode): path to file
        location (Point): Location of the photo
        description (text): Photo description
    """
    __tablename__ = 'photoss'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode(64))
    path = db.Column(db.Unicode(128))
    location = db.Column(Geometry("POINT", 926919))
    description = db.Column(db.Text)

    #incident_id = db.Column(db.Integer, db.ForeignKey('avalanche_ins.id'))
    #incident = db.relationship('AvalancheIn', backref='photos')

    def __unicode__(self):
        return self.name
