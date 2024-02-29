from pyramid.view import view_config
from samba.netcmd.domain.models import User


@view_config(route_name="home", renderer="home.jinja2")
def home(request):
    users = User.query(request.samdb)
    return {"project": "sambal", "users": users}
