from unittest.mock import Mock

from sambal.views.auth import login


def test_login_view(app_request):
    """A sample test that calls the login view directly.

    The 'real request' lacks a matched_route property required by the
    login view, which can be done in the test rather than fixture.
    """
    app_request.matched_route = Mock()
    context = login(app_request)
    assert "form" in context
    assert "return_url" in context
