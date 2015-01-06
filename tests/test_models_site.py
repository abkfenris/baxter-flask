from tests import TestCase

from baxter.models import Role
from baxter import db


class TestFrontend(TestCase):
    """
    Test the site models like Role and User
    """
    def test_roles_count(self):
        #print 'test_roles_count'
        assert Role.query.count() == 2
        db.session.commit()

    def test_roles(self):
        #print 'test roles'
        role = Role.query.filter_by(name='admin').first()
        #print 'query'
        assert role is not None
        #print 'assert'
        db.session.commit()
