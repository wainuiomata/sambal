from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.config import Configurator

from .client import get_samdb
from .security import get_authenticated_user, groupfinder
from .settings import SETTINGS

authn_policy = AuthTktAuthenticationPolicy(
    SETTINGS["authn.secret"],
    http_only=True,
    secure=False,
    callback=groupfinder,
    hashalg="sha512",
    samesite="Strict",
)

with Configurator(authentication_policy=authn_policy, settings=SETTINGS) as config:
    config.include("pyramid_jinja2")
    config.include("sambal.routes")
    config.include("pyramid_session_redis")
    config.add_jinja2_search_path("sambal:templates")
    config.add_request_method(get_samdb, "samdb", property=True, reify=True)
    config.add_request_method(get_authenticated_user, "user", property=True, reify=True)
    config.scan("sambal.views")
    app = config.make_wsgi_app()
