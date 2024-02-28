Sambal
------

Sambal is an experimental web interface for Samba using Pyramid.

At this point it is more just a proof of concept.

It requires the latest version of Samba master compiled from source,
because the Samba models haven't yet made it into a release.

At this point I just create a virtualenv and copy the compiled Samba
files inside it, it's crude but works.

    python3 -m venv venv
    cp -R samba/bin/python/* venv/site-packages/
    venv/bin/pip install -e .

Why Pyramid
-----------

Pyramid is an older framework, but it is super flexible, and we do have
quite a bit of experience with it. But the primary reason is that it
supports both URL-Dispatch and Traversal.

In this project we want to investigate using Traversal and mapping
URL parts to a DN seems to make sense.

We have therefore chosen to use Pyramid over Flask for this particular
project. As for "why not FastAPI" well Samba isn't exactly async so
that doesn't sound like the wisest choice.

License
-------

Sambal is released under GPL v3 which this the same license Samba uses.
