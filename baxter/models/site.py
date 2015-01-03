from .. import db
from flask.ext.security import UserMixin, RoleMixin, SQLAlchemyUserDatastore

roles_users = db.Table('roles_users',
                       db.Column('user_id',
                                 db.Integer(),
                                 db.ForeignKey('users.id')),
                       db.Column('role_id',
                                 db.Integer(),
                                 db.ForeignKey('roles.id')))


class Role(db.Model, RoleMixin):
    """
    Role Model

    Using Flask-Security's RoleMixin

    Arguments:
        id (int): Primary Role Key
        name (str): Role name for reference in admin and for restrictions
        description (str): Role description
    """
    __tablename__ = 'roles'

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))


class User(db.Model, UserMixin):
    """
    User model

    Using Flask-Security's UserMixin

    Arguments:
        id (int): Primary User Key
        username (str): Unique username as chosen by the user
        first (str): First name
        last (str): Last name
        email (str): User's email address
        active (bool): Is the user activated
        confirmed_at (Datetime): When was the user confirmed
        roles (list): List of role objects that the user has
        observer (bool): Is this user an official observer
        username (str): Prefered username
        avalanche_incidents (AvalancheIn): List of Avalanche Instances
        observations (WeatherOb): List of Weather Observations
        weather_forecasts (WeatherFor): List of Weather Forecasts
        involved (AvalancheInvolved): List of Avalanches Incidents that user is involved with
    """
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime())

    roles = db.relationship('Role', secondary=roles_users,
                            backref=db.backref('users', lazy='dynamic'))

    observer = db.Column(db.Boolean, default=False)
    username = db.Column(db.String(80), unique=True)
    first = db.Column(db.String(80))
    last = db.Column(db.String(80))

    def __repr__(self):
        return '<User %r>' % self.username

user_datastore = SQLAlchemyUserDatastore(db, User, Role)
