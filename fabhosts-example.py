"""
Define hosts for fab to use
"""

from fabric.api import env


def prod():
    env.user = 'user'
    env.hosts = [
        'host.com',
    ]
