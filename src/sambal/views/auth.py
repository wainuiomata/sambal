from pyramid.httpexceptions import HTTPFound
from pyramid.view import forbidden_view_config, view_config

from sambal.forms import LoginForm
from sambal.security import login, logout


@view_config(route_name="login", renderer="login.jinja2")
@forbidden_view_config(accept="text/html", renderer="login.jinja2")
def login_view(request):
    """Login form."""
    # Avoid looping the login page if accessed directly.
    if request.matched_route.name == "login":
        return_url = request.route_url("home")
    else:
        return_url = request.POST.get("return_url", request.url)

    if request.method == "POST":
        if (form := LoginForm(request.POST)) and form.validate():
            username = form.username.data
            password = form.password.data
            host = form.host.data
            realm = form.realm.data

            if headers := login(request, username, password, host, realm):
                return HTTPFound(location=return_url, headers=headers)
            else:
                request.session.flash("Login to host failed", queue="error")
    else:
        form = LoginForm()

    return {
        "return_url": return_url,
        "form": form,
    }


@view_config(route_name="logout")
def logout_view(request):
    """Logout user."""
    headers = logout(request)
    redirect_url = request.route_url("home")
    return HTTPFound(location=redirect_url, headers=headers)
