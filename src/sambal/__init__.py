from pyramid.config import Configurator

from .client import get_samdb
from .settings import SETTINGS

with Configurator(settings=SETTINGS) as config:
    config.include("pyramid_jinja2")
    config.include("sambal.routes")
    config.include("pyramid_session_redis")
    config.add_jinja2_search_path("sambal:templates")
    config.add_request_method(get_samdb, "samdb", property=True, reify=True)
    config.scan("sambal.views")
    app = config.make_wsgi_app()
