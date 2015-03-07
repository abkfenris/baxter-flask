Makefile
========

A Makefile is provided for some common tasks, mostly pertaining to documentation.


Building Documentation
----------------------

When creating documentation use ``make build`` to render it into the `docs/html`
directory. If you're awesome enough that you wish to have your docs in a
different format, just type ``make help``.



Hosting Documentation on GitHub
-------------------------------

GitHub is awesome and will host Jekyll sites and static HTML sites for free.
``make ghp`` will build the docs and drop them into a ``github-pages`` branch,
that you can push to GitHub at your lesiure.
