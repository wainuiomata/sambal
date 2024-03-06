Sambal
------

Sambal is an experimental web interface for Samba and Active Directory
domains using Pyramid.

At this point it is more just a proof of concept.

It requires the latest version of Samba master compiled from source,
because the Samba models haven't yet made it into a release.

At this point I just create a virtualenv and copy the compiled Samba
files inside it, it's crude but works.

    python3 -m venv venv
    cp -R samba/bin/python/* venv/site-packages/
    . venv/bin/activate
    pip install -e .

Configuring Sambal
------------------

You will need a Redis server for sessions which must be properly secured.
See the [Configuration](https://github.com/wainuiomata/sambal/wiki/Configuration)
page on the Wiki for more details.

Starting Sambal
---------------

To start a development server just run:

    python3 -m sambal

The web interface can then be accessed at http://localhost:8000

To start a production server, first install sambal without -e as that is
meant to be used for development only.

    pip install .

Then also install gunicorn and run:

    pip install gunicorn
    gunicorn sambal:app -w 4

Why Pyramid
-----------

Pyramid is an older framework, but it is super flexible, and we do have
quite a bit of experience with it. But the primary reason is that it
supports both URL-Dispatch and Traversal.

In this project we want to investigate using Traversal and mapping
URL parts to a DN seems to make sense.

License
-------

Sambal is released under the [GPL v3](LICENSE.txt) license which is the
same license that Samba uses.
