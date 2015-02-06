fabfile.py
==========

`Fabric <http://www.fabfile.org>`_ is basically a makefile, except has server
management built in. Being able to run ``fab prod deploy`` to send your latest
modification to the server is sweet. It also is a great way to document common
tasks that you do when managing servers, without writing the whole process up in
Sphinx or elsewhere.

* `Hosts`_
* `Deploying Changes`_
* `Rolling Back Changes`_
* `Checking Server Status`_
* `Running the Server`_
* `Adding Users to Site`_
* `Creating Roles`_
* `Setting Up a New Server`_

Hosts
-----

Fabric seems to work best when you can login into a host with ssh keys, and
have sudo rights. So that the ``fabfile.py`` can be in source control, but
host information can be left out, the fabfile can get hosts from ``fabhosts.py``.

To create ``fabhost.py`` either copy and modify ``fabhost-example.py`` or write
along these lines:

.. code-block:: python

    from fabric.api import env

    def prod():
        env.user = 'user'
        env.hosts = [
            'host.com',
        ]

Then to run fabric with those hosts, just ``fab prod <command>``.

If you are awesome enough to have staging servers or other groups of server that
you will be commanding, define another command in ``fabhosts.py`` and modify
``fabfile.py`` import statement

.. code-block:: python

    try:
        from fabhost import prod, staging
    except ImportError:
        pass


Deploying Changes
-----------------

After making some changes to the code, they can be pushed to the server(s) with
``fab deploy`` which will ask for a commit message.

Here's what happens when I deploy the changes that I just wrote (meta much?):

.. code-block:: bash

    $ fab prod deploy
    [baxter.alexkerney.com] Executing task 'deploy'
    [localhost] local: git add -A
    Commit message? Working on fabfile documentation
    [localhost] local: git commit -am "Working on fabfile documentation"
    [master 6d52e86] Working on fabfile documentation
     40 files changed, 161 insertions(+), 8 deletions(-)
     rewrite docs/doctrees/developers/fabfile.doctree (98%)
     rewrite docs/doctrees/developers/index.doctree (63%)
     rewrite docs/html/searchindex.js (97%)
    [localhost] local: git push production master
    Counting objects: 126, done.
    Delta compression using up to 8 threads.
    Compressing objects: 100% (126/126), done.
    Writing objects: 100% (126/126), 181.58 KiB | 0 bytes/s, done.
    Total 126 (delta 75), reused 0 (delta 0)
    To root@baxter.alexkerney.com:/home/git/baxter-flask.git
       3d583d7..6d52e86  master -> master
    [baxter.alexkerney.com] sudo: supervisorctl restart baxter_flask
    [baxter.alexkerney.com] out: baxter_flask: stopped
    [baxter.alexkerney.com] out: baxter_flask: started
    [baxter.alexkerney.com] out:


    Done.
    Disconnecting from baxter.alexkerney.com... done.

.. warning::
    ``fab deploy`` does not run database migrations. If there are any changes to
    database schema, then the site should be deployed, stopped, migrated, and
    started again.


Rolling Back Changes
--------------------

Every once in a while mistakes happen. ``fab rollback`` can help clean up some
of them if they have already been deployed.


Checking Server Status
----------------------

``fab status`` will check the supervisor processes, nginx, postgres, and ufw
firewall statuses.

.. code-block:: bash

    $ fab prod status
    [baxter.alexkerney.com] Executing task 'status'
    [baxter.alexkerney.com] sudo: supervisorctl status
    [baxter.alexkerney.com] out: baxter_flask                     RUNNING    pid 19223, uptime 0:15:20
    [baxter.alexkerney.com] out:

    [baxter.alexkerney.com] sudo: service nginx status
    [baxter.alexkerney.com] out:  * nginx is running
    [baxter.alexkerney.com] out:

    [baxter.alexkerney.com] sudo: service postgresql status
    [baxter.alexkerney.com] out: 9.4/main (port 5432): online
    [baxter.alexkerney.com] out:

    [baxter.alexkerney.com] sudo: service ufw status
    [baxter.alexkerney.com] out: ufw start/running
    [baxter.alexkerney.com] out:


    Done.
    Disconnecting from baxter.alexkerney.com... done.



Running the Server
------------------

``fab run_app`` will get supervisor to kick off gunicorn and flask.



Adding Users to Site
--------------------

Instead of sshing into the server and using ``manage.py``, ``fab`` can also
setup users with ``fab add_baxter_user``. It will ask for email address,
password, and if that user should be an admin, which defaults to no.

.. code-block:: bash

    $ fab prod add_baxter_user
    [baxter.alexkerney.com] Executing task 'add_baxter_user'
    Email address: test@server.com
    Password: password
    Is test@server.com an admin? [y/N] y
    [baxter.alexkerney.com] sudo: python manage.py user create_user -e test@server.com -p password -a y
    [baxter.alexkerney.com] out: User created successfully.
    [baxter.alexkerney.com] out: {
    [baxter.alexkerney.com] out:     "active": true,
    [baxter.alexkerney.com] out:     "email": "test@server.com",
    [baxter.alexkerney.com] out:     "password": "****"
    [baxter.alexkerney.com] out: }
    [baxter.alexkerney.com] out:

    [baxter.alexkerney.com] sudo: python manage.py user add_role -u test@server.com -r admin
    [baxter.alexkerney.com] out: Role 'admin' added to user 'test@server.com' successfully
    [baxter.alexkerney.com] out:


    Done.
    Disconnecting from baxter.alexkerney.com... done.


Creating Roles
--------------

Fabric can setup all the roles that the server should start with using
``fab create_roles``.


Setting Up a New Server
-----------------------

At some point ``fab create`` will configure a server for you, but currently only
a few parts of it work, so running individual steps and configuring things via
ssh is the best option. Currently none of these are tested so procede at your
own risk.

.. literalinclude:: ../../fabfile.py
    :pyobject: create

#. Install basic requirements - ``fab install_requirements``
    .. literalinclude:: ../../fabfile.py
        :pyobject: install_requirements

#. Setup www User
    I believe ``chpasswd`` requires ``user:pass`` to be read in from a file.

    .. literalinclude:: ../../fabfile.py
        :pyobject: create_www_user

#. Create Database and Postgres User
    .. literalinclude:: ../../fabfile.py
        :pyobject: setup_database

#. Install Flask environment and requirements - ``fab install_flask``
    .. literalinclude:: ../../fabfile.py
        :pyobject: install_flask

#. Configure nginx site - ``fab configure_nginx``
    .. literalinclude:: ../../fabfile.py
        :pyobject: configure_nginx

#. Make environment variables file.
#. Configure gunicorn starter - ``fab configure_gunicorn``
    .. literalinclude:: ../../fabfile.py
        :pyobject: configure_gunicorn

#. Configure Supervisor - ``fab configure_supervisor``
    .. literalinclude:: ../../fabfile.py
        :pyobject: configure_supervisor

#. Configure Git to recieve pushes and restart server for deploys - ``fab configure_git``
    .. literalinclude:: ../../fabfile.py
        :pyobject: configure_git
