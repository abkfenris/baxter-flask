manage.py
=========

During development and server setup, you can use ``manage.py`` to run the server,
setup users, modify the database, and see http routes. Also makes it easy to get
a Python or IPython shell with an app context.

* `Running the Server`_
* `Listing HTTP Routes`_
* `Opening a Shell`_
* `Working with Users and Roles`_
    * `Roles`_
    * `Users`_
* `Database Operations`_

Running the Server
------------------

To quickly launch the server use ``python manage.py runserver``

.. code-block:: bash

    $ python manage.py runserver
     * Running on http://127.0.0.1:5000/
     * Restarting with reloader

Listing HTTP Routes
-------------------

``python manage.py list_routes`` will list the blueprints, HTTP methods, and the
endpoints that are avaliable.

.. code-block:: bash

    $ python manage.py list_routes
    main.avalanche_incident                            HEAD,OPTIONS,GET     /avalanche/incident/<int:id>
    main.avalanche_incidents                           HEAD,OPTIONS,GET     /avalanche/incident/
    main.avalanche_path                                HEAD,OPTIONS,GET     /avalanche/path/<id>/
    main.avalanche_paths                               HEAD,OPTIONS,GET     /avalanche/path/
    main.index                                         HEAD,OPTIONS,GET     /
    main.trail                                         HEAD,OPTIONS,GET     /trails/<id>/
    main.trails                                        HEAD,OPTIONS,GET     /trails/
    ...


Opening a Shell
---------------

``manage.py`` can open a Python or IPython (default if avaliable) shell, with
many things imported:

* ``app``
* ``db``
* ``User``
* ``Role``
* ``WeatherOb``
* ``WeatherFor``
* ``Trail``
* ``POI``
* ``AvalnchePath``
* ``AvalancheInvolved``
* ``AvlancheIn``
* ``AvalancheProb``
* ``AvalancheInProb``

.. code-block:: bash

    $ python manage.py shell

.. code-block:: python

    In [1]:

Working with Users and Roles
----------------------------

``manage.py`` is able to manage users and roles on the server.

Roles
^^^^^

Before a user can be assigned a role, the role must exist, so create one with
``python manage.py user create_role``

.. program:: create_role
.. option:: -n <name>, --name <name>

    Name of role

.. option:: -d <description>, --description <description>

    Description of role

For example, to create an admin role:

.. code-block:: bash

    $ python manage.py user create_role -n admin

    Role admin created successfully.

Right now only an ``admin`` role is defined on the site, but others will be
setup in the future.

Users
^^^^^

You can create a user without `Roles`_ existing, but it makes sense to have them
setup first. Once roles are setup ``python manage.py user create_user`` allows
you to create a new account based on an email address.

.. program:: create_user
.. option:: -u <name@server.com>, --user <name@server.com>

    User name

.. option:: -p <password>, --password <password>

    Password

.. option:: -a <y> or <active>, --active <y> or <active>

    Is the user activated and allowed to log in?

For example, to add and activate a user:

.. code-block:: bash

    $ python manage.py user create_user -u test@server.com -p password -y a

    User created sucessfully.
    {
        "active": true,
        "email": "test@server.com",
        "password": "****"
    }

To give a user a specific role ``python manage.py user add_role`` is used

.. program: add_role
.. option:: -u <name@server.com> or --user <name@server.com>

    Email address for user that you wish to add the role too

.. option: --r <role> or --role <role>

    Name of role to add to the user

If we wanted the user that we just created to be an admin:

.. code-block:: bash

    $ python manage.py user add_role -u test@server.com -r admin
    Role 'admin' added to user 'test@server.com' successfully


Other user focused commands include ``activate_user`` and ``deactivate_user`` if
you didn't explicitly activate a user upon account creation, or someone has been
misbehaving.

.. option:: -u <name@server.com> or --user <name@server.com>

    Email address for the user that you wish to modify

``remove_role`` is to remove a role from a user

.. option:: -u <name@server.com> or --user <name@server.com>

    Email address for the user that you wish to remove the role from

.. option: --r <role> or --role <role>

    Name of role to remove from a user


Database Operations
-------------------

``manage.py`` also handles modification and setup of the database, based on code
changes. Each change creates a new migration file.

See `flask-Migrate <http://flask-migrate.readthedocs.org>`_ for more information.
