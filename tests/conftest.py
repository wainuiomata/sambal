import os

import pytest
import webtest
from pyramid.scripting import prepare

import sambal


@pytest.fixture(scope="session")
def settings():
    """Fixture that returns the Pyramid settings dict."""
    test_settings = dict(sambal.SETTINGS)
    test_settings["samba.host"] = os.getenv("SAMBAL_TEST_HOST")
    test_settings["samba.username"] = os.getenv("SAMBAL_TEST_USERNAME")
    test_settings["samba.password"] = os.getenv("SAMBAL_TEST_PASSWORD")
    test_settings["samba.realm"] = os.getenv("SAMBAL_TEST_REALM")
    test_settings["http_host"] = "example.com"
    return test_settings


@pytest.fixture(scope="session")
def app():
    """Fixtures that returns the Sambal WSGI app."""
    return sambal.app


@pytest.fixture
def testapp(app, settings):
    """Fixture that returns a Sambal WebTest app."""
    return webtest.TestApp(
        app,
        extra_environ={
            "HTTP_HOST": settings["http_host"],
        },
    )


@pytest.fixture
def app_request(app):
    """Returns a real HTTP request for use with testing Sambal views."""
    with prepare(registry=app.registry) as env:
        req = env["request"]
        req.host = "example.com"
        yield req
