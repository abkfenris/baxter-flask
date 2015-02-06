API
===

There is a public API to access this server via REST. Right now it is relatively
simple, but the ability to get different types of data, and hopefully submit
data is in the plans.

.. autoflask:: baxter:create_app('default')
    :endpoints:
    :blueprints: api
