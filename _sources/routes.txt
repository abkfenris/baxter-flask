HTTP Routes for site
====================

.. toctree::

Browseable routes
-----------------

.. autoflask:: baxter:create_app('default')
    :endpoints:
    :blueprints: main
    :undoc-static:

API routes
----------

.. autoflask:: baxter:create_app('default')
    :endpoints:
    :blueprints: api
