from pyramid.view import view_config
from samba.netcmd.domain.models import Computer


@view_config(route_name="home", renderer="home.jinja2")
def home(request):
    computers = Computer.query(request.samdb)
    return {"project": "sambal", "computers": computers}
