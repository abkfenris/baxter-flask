Baxter User Help
================

.. toctree::

Some quick notes about using the site

Markdown
--------
In places which will generate longer text blurbs, like the description of an
Avalanche Incident, can be formatted as `Markdown <https://help.github.com/articles/markdown-basics/>`_.

Markdown is a more human readable, and natural way of formatting text compared
to writing html.

Links
^^^^^
Links are very easily formatted in Markdown. Just insert ``[link text](link url)``
into the description. Example: ::

    [National Avalanche Center](http://www.fsavalanche.org)

Will be formatted into: ::

    <a href="http://www.fsavalanche.org">National Avalanche Center</a>

And displayed as `National Avalanche Center <http://www.fsavalanche.org>`_

Images
^^^^^^
Images uploaded via the admin will be in ``/static/uploaded/photos/``. To get
the path of an image, check Admin/Photos list for the path.

.. image:: _static/user-image-path.png
   :scale: 50 %

If you are in the in the process of uploading images within an Avalanche
Incident or other location, then you'll need to finish up and save before the
image is uploaded to the server, and the path becomes visible.

To insert an image into the markdown type ``![caption](path)``.

For example: ::

    ![Photo of Devil's Den](/static/uploaded/photos/IMG_2774.jpg)

Gets turned into this code which will nicely render an image: ::

    <img src="/static/uploaded/photos/IMG_2774.jpg" alt="Photo of Devil's Den" class="img-responsive">

Currently images are only setup to be displayed at full size.
