import pytest
import webtest
from pyramid.scripting import prepare


@pytest.fixture(scope="session")
def app():
    """Fixtures that returns the Sambal WSGI app.

    We can inject env vars here if necessary, but only before the import.
    """
    import sambal

    return sambal.app


@pytest.fixture
def testapp(app):
    """Fixture that returns a Sambal WebTest app."""
    return webtest.TestApp(
        app,
        extra_environ={
            "HTTP_HOST": "example.com",
        },
    )


@pytest.fixture
def app_request(app):
    """Returns a real HTTP request for use with testing Sambal views."""
    with prepare(registry=app.registry) as env:
        req = env["request"]
        req.host = "example.com"
        yield req
