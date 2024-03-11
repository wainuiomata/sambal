from ldb import LdbError
from pyramid.httpexceptions import HTTPFound
from pyramid.view import forbidden_view_config, view_config

from sambal.forms import LoginForm


@view_config(route_name="login", renderer="login.jinja2")
@forbidden_view_config(accept="text/html", renderer="login.jinja2")
def login(request):
    """Login form."""
    if request.method == "POST":
        return_url = request.POST.get("return_url", request.path)

        if (form := LoginForm(request.POST)) and form.validate():
            username = form.username.data
            password = form.password.data
            host = form.host.data
            realm = form.realm.data

            try:
                if headers := request.login(host, username, password, realm):
                    return HTTPFound(location=return_url, headers=headers)
                else:
                    request.session.flash("Login failed", queue="error")

            except LdbError as e:
                msg = e.args[1]
                request.session.flash(f"Login failed: {msg}", queue="error")
    else:
        # Avoid looping the login page if accessed directly.
        # Also, as the app uses traversal request.matched_route can be None.
        if request.matched_route and request.matched_route.name == "login":
            return_url = request.route_path("home")
        else:
            return_url = request.path

        form = LoginForm()

    return {
        "return_url": return_url,
        "form": form,
    }


@view_config(route_name="logout")
def logout(request):
    """Logout user."""
    headers = request.logout()
    redirect_url = request.route_url("home")
    return HTTPFound(location=redirect_url, headers=headers)
