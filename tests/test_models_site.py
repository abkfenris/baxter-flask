from tests import TestCase

from baxter.models import Role, User
from baxter import db


class TestFrontend(TestCase):
    """
    Test the site models like Role and User
    """
    def test_roles_count(self):
        #print 'test_roles_count'
        assert Role.query.count() == 2

    def test_roles(self):
        #print 'test roles'
        role = Role.query.filter_by(name='admin').first()
        #print 'query'
        assert role is not None
        #print 'assert'

    def test_users_count(self):
        count = User.query.count()
        print count
        assert count == 1

    def test_user_roles(self):
        user = User.query.filter_by(email='test@domain.com').first()
        print user.roles
        assert len(user.roles) is 1
