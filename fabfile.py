from fabric.api import cd, env, lcd, put, prompt, local, sudo

# config

local_app_dir = './baxter'

remote_app_dir = '/home/www'
remote_git_dir = '/home/git'
remote_flask_dir = remote_app_dir + '/baxter'
remote_nginx_dir = '/etc/nginx/sites-enabled'
remote_supervisor_dir = '/etc/supervisor/conf.d'

# tasks


def run_app():
    """
    Run the app
    """
    with cd(remote_flask_dir):
        sudo('supervisorctl start baxter_flask')


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
