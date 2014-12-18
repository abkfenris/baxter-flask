#!/usr/bin/env python
import os
COV = None
#!/usr/bin/env python
import os
COV = None
if os.environ.get('FLASK_COVERAGE'):
	import coverage
	COV = coverage.coverage(branch=True, include='app/*')
	COV.start()

from flask import url_for, Flask
from baxter import create_app, db
from baxter.models import User, Role, WeatherOb, WeatherFor, Trail, POI, AvalanchePath
# from baxter.models import 
from flask.ext.script import Manager, Shell
import config
from flask.ext.migrate import Migrate, MigrateCommand
from flask.ext.security.script import CreateUserCommand, CreateRoleCommand, AddRoleCommand, RemoveRoleCommand, ActivateUserCommand, DeactivateUserCommand

app = create_app('default')
manager = Manager(app)
migrate = Migrate(app, db)

def sub_opts(app, **kwargs):
	pass
user_manager_desc = ("'user create_user --email name@server.com --password initialpass'" + '\n'
	+'words')
user_manager = Manager(sub_opts, usage='User and role management', description=user_manager_desc)

class CreateUserC(CreateUserCommand):
	"""
	Create a user: -e or --email name@server.com, -p or --password initialpass, -a or --active y or active
	"""
	pass
class CreateRoleC(CreateRoleCommand):
	"""
	Create a role: -n or --name role_name, -d or --desc role_description
	"""
	pass
class AddRoleC(AddRoleCommand):
	"""
	Add a role to a user: -u or --user name@server.com, -r or --role role_name
	"""
	pass



user_manager.add_command('create_user', CreateUserC())
user_manager.add_command('create_role', CreateRoleC())
user_manager.add_command('add_role', AddRoleC())

manager.add_command('user', user_manager)


manager.add_command('db', MigrateCommand)

def make_shell_context():
	return dict(app=app, db=db, User=User, WeatherOb=WeatherOb, WeatherFor=WeatherFor, Trail=Trail, POI=POI, AvalanchePath=AvalanchePath)
manager.add_command('shell', Shell(make_context=make_shell_context))


# http://flask.pocoo.org/snippets/117/ manager helper to list routes http://stackoverflow.com/questions/13317536/get-a-list-of-all-routes-defined-in-the-app
@manager.command
def list_routes():
	"""
	Lists routes for app
	"""
	import urllib
	
	output = []
	for rule in app.url_map.iter_rules():
		methods = ','.join(rule.methods)
		line = urllib.unquote("{:50s} {:20s} {}".format(rule.endpoint, methods, rule))
		output.append(line)
	
	for line in sorted(output):
		print(line)

if __name__ == '__main__':
	manager.run()