#!/usr/bin/env python
import os
COV = None
COV = None
if os.environ.get('FLASK_COVERAGE'):
    import coverage
    COV = coverage.coverage(branch=True, include='app/*')
    COV.start()

from baxter import create_app, db
from baxter.models import (User, Role,
                           WeatherOb, WeatherFor,
                           Trail, POI,
                           AvalanchePath, AvalancheInvolved,
                           AvalancheIn, AvalancheProb,
                           AvalancheInProb)
from baxter.user_manager import user_manager
# from baxter.models import
from flask.ext.script import Manager, Shell
import config
from flask.ext.migrate import Migrate, MigrateCommand

if os.environ.get('BAXTER_FLASK_ENV') == 'prod':
    app = create_app('production')
else:
    app = create_app('default')
manager = Manager(app)
migrate = Migrate(app, db)

# Adds Flask-admin user management commands
manager.add_command('user', user_manager)


manager.add_command('db', MigrateCommand)


def make_shell_context():
    return dict(app=app, db=db, User=User, Role=Role,
                WeatherOb=WeatherOb, WeatherFor=WeatherFor,
                Trail=Trail, POI=POI, AvalanchePath=AvalanchePath,
                AvalancheInvolved=AvalancheInvolved,
                AvalancheIn=AvalancheIn, AvalancheProb=AvalancheProb,
                AvalancheInProb=AvalancheInProb)
manager.add_command('shell', Shell(make_context=make_shell_context))


# http://flask.pocoo.org/snippets/117/ manager helper to list routes
# http://stackoverflow.com/questions/13317536/get-a-list-of-all-routes-defined-in-the-app
@manager.command
def list_routes():
    """
    Lists routes for app
    """
    import urllib

    output = []
    for rule in app.url_map.iter_rules():
        methods = ','.join(rule.methods)
        line = urllib.unquote("{:50s} {:20s} {}".format(rule.endpoint,
                                                        methods,
                                                        rule))
        output.append(line)

    for line in sorted(output):
        print(line)

if __name__ == '__main__':
    manager.run()
