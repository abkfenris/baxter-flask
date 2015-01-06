from tests import TestCase

from baxter.models import Trail
from baxter import db


class TestFrontend(TestCase):
    """
    Test the front end of the site
    """
    def test_show(self):
        #print 'test_show'
        rv = self.app.test_client().get('/')
        assert 'Baxter' in rv.data
        self.assert_200(rv)

    def test_login(self):
        rv = self.app.test_client().get('/admin/', follow_redirects=True)
        assert 'Login' in rv.data

    def test_trails_view(self):
        rv = self.app.test_client().get('/trails/')
        assert 'Trails</h1>' in rv.data
