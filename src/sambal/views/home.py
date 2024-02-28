from pyramid.view import view_config


@view_config(route_name="home", renderer="home.jinja2")
def home(request):
    return {"project": "sambal"}
