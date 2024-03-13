from pyramid.config import Configurator
from pyramid.csrf import SessionCSRFStoragePolicy

from .client import get_samdb
from .security import SambalSecurityPolicy, login, logout
from .settings import SETTINGS

with Configurator(settings=SETTINGS) as config:
    config.include("pyramid_jinja2")
    config.include("sambal.renderers")
    config.include("sambal.routes")
    config.include("pyramid_session_redis")
    config.set_csrf_storage_policy(SessionCSRFStoragePolicy())
    config.set_default_csrf_options(require_csrf=True)
    config.set_security_policy(SambalSecurityPolicy(SETTINGS))
    config.add_tween("sambal.tweens.SecurityHeaders")
    config.add_jinja2_search_path("sambal:templates")
    config.add_request_method(get_samdb, "samdb", property=True, reify=True)
    config.add_request_method(login, "login")
    config.add_request_method(logout, "logout")
    config.scan("sambal.resources")
    config.scan("sambal.views")
    app = config.make_wsgi_app()
