"""
Fabric commands to setup and run server

Copy fabhosts-example.py to fabhosts.py and add host configurations for
your deployment.
"""

from fabric.api import cd, env, lcd, put, prompt, local, sudo, prefix
from fabric.contrib.files import exists
from fabric.contrib.console import confirm

try:
    from fabhosts import prod
except ImportError:
    pass

# config

local_app_dir = '.'
local_flask_dir = local_app_dir + '/baxter'
local_config_dir = local_app_dir + '/server-config'

remote_app_dir = '/home/www/baxter-flask'
remote_git_dir = '/home/git'
remote_flask_dir = remote_app_dir + '/baxter'
remote_nginx_dir = '/etc/nginx/sites-enabled'
remote_supervisor_dir = '/etc/supervisor/conf.d'

# tasks

def install_requirements():
    """
    Install required system wide packages.

    Includes exporting some info so GDAL can be used to build in pip
    http://gis.stackexchange.com/questions/28966/python-gdal-package-missing-header-file-when-installing-via-pip
    """
    sudo('apt-get update')
    sudo('apt-get upgrade')
    sudo('apt-get install -y python python-dev python-pip python-virtualenv')
    sudo('apt-get install -y nginx')
    sudo('apt-get install -y postgresql-9.4 postgresql-9.4-postgis-2.1')
    sudo('apt-get install -y postgresql-server-dev-9.4')
    sudo('apt-get install -y libpq-dev')
    sudo('apt-get install -y git')
    sudo('apt-get install -y gdal-bin python-gdal libgdal-dev')
    sudo('apt-get install -y supervisor')
    sudo('apt-get install -y redis-server')
    sudo('apt-get install -y libxslt1.dev')
    # for pillow
    sudo('apt-get install -y libjpeg8-dev libjpeg-dev libfreetype6-dev')
    sudo('apt-get install -y zlib1g-dev libpng12-dev')
    # So that GDAL can be built
    sudo('export CPLUS_INCLUDE_PATH=/usr/include/gdal')
    sudo('export C_INCLUDE_PATH=/usr/include/gdal')


def create_www_user():
    """
    Create a user for running it
    """
    password = prompt('Password for baxter-www user?')
    sudo('adduser --quiet baxter-www')
    sudo('chpasswd '.format(password))
    # not finished


def setup_database():
    """
    Setup postgres database with postgis extension
    """
    with cd('/'):
        sudo('su postgres')
        # not finished


def install_flask():
    """
    1. Create project directories
    2. Create and activeate a virtualenv
    3. Copy Flask files to remote host
    """
    if exists(remote_app_dir) is False:
        sudo('mkdir ' + remote_app_dir)
    if exists(remote_flask_dir) is False:
        sudo('mkdir' + remote_flask_dir)
    with lcd(local_app_dir):
        with cd(remote_app_dir):
            sudo('virtualenv ../env')
            sudo('source ../env/bin/activate')
            put('*', './', use_sudo=True)
            sudo('pip install -r requirements.txt')
            sudo('pip install PIL --allow-external PIL --allow-unverified PIL')


def configure_nginx():
    """
    1. Remove default nginx config file
    2. Create new config file
    3. Setup new symbolic link
    4. Copy local config to remote config
    5. Restart nginx
    """
    sudo('service nginx start')
    if exists('/etc/nginx/sites-enabled/default'):
        sudo('rm /etc/nginx/sites-enabled/default')
    if exists('/etc/nginx/sites-available/baxter-flask') is False:
        sudo('touch /etc/nginx/sites-available/baxter-flask')
        sudo('ln -s /etc/nginx/sites-available/baxter-flask' +
             ' /etc/nginx/sites-enabled/baxter-flask')
    with lcd(local_config_dir):
        with cd(remote_nginx_dir):
            put('./baxter-flask', './', use_sudo=True)
    sudo('service nginx restart')


def configure_supervisor():
    """
    1. Create new supervisor config file
    2. Copy local config to remote config
    3. Register new command
    """
    if exists('/etc/supervisor/conf.d/baxter_flask.conf') is False:
        with lcd(local_config_dir):
            with cd(remote_supervisor_dir):
                put('baxter_flask.conf', './', use_sudo=True)
                sudo('supervisorctl reread')
                sudo('supervisorctl update')


def configure_git():
    """
    1. Setup bare Git repo
    2. Create post-recieve hook
    """
    if exists(remote_git_dir) is False:
        sudo('mkdir ' + remote_git_dir)
        with cd(remote_git_dir):
            sudo('mkdir baxter-flask.git')
            with cd('baxter-flask.git'):
                sudo('git init --bare')
                with lcd(local_config_dir):
                    with cd('hooks'):
                        put('./post-receive', './', use_sudo=True)
                        sudo('chmod +x post-receive')


def configure_gunicorn():
    """
    1. Setup gunicorn starter file
    """
    if exists('/home/www/gunicorn-start-baxter') is False:
        with cd(remote_app_dir):
            with lcd(local_config_dir):
                put('./gunicorn-start-baxter', './', use_sudo=True)
                sudo('chmod +x gunicorn-start-baxter')


def configure_ufw():
    """
    1. Allow ssh, http, https, and postgres connections through ufw
    2. Enable ufw
    """
    sudo('ufw allow ssh')
    sudo('ufw allow www')
    sudo('ufw allow https')
    sudo('ufw allow postgres')
    sudo('ufw enable')

def create():
    """
    Setup a brand new server
    """
    install_requirements()
    install_flask()
    configure_gunicorn()
    configure_nginx()
    configure_supervisor()
    configure_git()


def run_app():
    """
    Run the app
    """
    with cd(remote_flask_dir):
        sudo('supervisorctl start baxter_flask')


def create_roles():
    """
    Create roles for users
    """
    with cd(remote_app_dir):
        with prefix('source /home/www/baxter-flask/server-config/host-export'):
            with prefix('source /home/www/env/bin/activate'):
                sudo('python manage.py user create_role -n admin')
                sudo('python manage.py user create_role -n user')
                sudo('python manage.py user create_role -n contributor')


def deploy():
    """
    1. Commit and push new flask files to production
    2. Restart gunicorn via supervisor on production
    """
    with lcd(local_app_dir):
        local('git add -A')
        commit_message = prompt('Commit message?')
        local('git commit -am "{0}"'.format(commit_message))
        local('git push production master')
        sudo('supervisorctl restart baxter_flask')


def rollback():
    """
    1. Quick rollback in case of error
    2. Restart gunicorn via supervisor
    """
    with lcd(local_app_dir):
        local('git revert master --no-edit')
        local('git push production master')
        sudo('supervisorctl restart baxter_flask')


def status():
    """
    Is the app live?
    """
    sudo('supervisorctl status')
    sudo('service nginx status')
    sudo('service postgresql status')
    sudo('service ufw status')
    sudo('service redis-server status')


def add_baxter_user():
    """
    Add a user to the website
    """
    with cd(remote_app_dir):
        with prefix('source /home/www/baxter-flask/server-config/host-export'):
            with prefix('source /home/www/env/bin/activate'):
                email = prompt('Email address:')
                password = prompt('Password:')
                admin = confirm('Is {0} an admin?'.format(email), default=False)
                sudo('python manage.py user create_user -e {0} -p {1} -a y'.format(email, password))
                if admin:
                    sudo('python manage.py user add_role -u {0} -r admin'.format(email))
