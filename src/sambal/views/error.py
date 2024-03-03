from pyramid.view import notfound_view_config


@notfound_view_config(renderer="404.jinja2", append_slash=True)
def notfound(request):
    request.response.status = 404
    return {}
