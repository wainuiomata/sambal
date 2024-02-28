from pyramid.config import Configurator


with Configurator() as config:
    config.include("pyramid_jinja2")
    config.include("sambal.routes")
    config.scan("sambal.views")
    app = config.make_wsgi_app()
