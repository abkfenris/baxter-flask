"""
Unit testing base using Flask-testing
https://github.com/imwilsonxu/fbone/blob/master/tests/__init__.py
"""

from flask.ext.testing import TestCase as Base, Twill

from baxter import create_app, db, create_db_and_roles
from baxter.models import Role, User, user_datastore


class TestCase(Base):
    """
    Base testcase for Baxter
    """

    def create_app(self):
        """
        Creates and returns a testing flask app
        """

        app = create_app('testing')
        return app

    def init_data(self):
        """
        Creates roles and users
        """

        # Roles
        admin_r = user_datastore.find_or_create_role('admin')
        db.session.commit()
        user_r = user_datastore.find_or_create_role('user')
        db.session.commit()


    def setUp(self):
        """
        Resets all tables before testing.
        """
        db.create_all()
        self.init_data()

    def tearDown(self):
        """
        Cleans up db session and drop all tables.
        """
        db.drop_all()

    def login(self, username, password):
        data = {
            'login': username,
            'password': password,
        }
        response = self.client.post('/login', data=data, follow_redirects=True)
        return response

    def _logout(self):
        response = self.client.get('/logout')
        self.assertRedirects(response, location='/')

    def _test_get_request(self, endpoint, template=None):
        response = self.client.get(endpoint)
        self.assert_200(response)
        if template:
            self.assertTemplateUsed(name=template)
        return response
