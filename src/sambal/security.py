from typing import Optional

from pyramid.authentication import AuthTktCookieHelper
from pyramid.interfaces import ISecurityPolicy
from pyramid.security import forget, remember
from samba.netcmd.domain.models import User
from zope.interface import implementer

from .client import connect_samdb
from .settings import USE_HTTPS


@implementer(ISecurityPolicy)
class SambalSecurityPolicy:
    def __init__(self, secret):
        self.authtkt = AuthTktCookieHelper(
            secret=secret,
            secure=USE_HTTPS,
            samesite="Strict",
            http_only=True,
        )

    def identity(self, request) -> Optional[User]:
        object_sid = self.authenticated_userid(request)
        if object_sid:
            return User.get(request.samdb, object_sid=object_sid)

    def authenticated_userid(self, request) -> Optional[str]:
        if request.samdb:
            return request.samdb.connecting_user_sid

    def permits(self, request, context, permission):
        return request.identity is not None

    def remember(self, request, userid, **kwargs):
        return self.authtkt.remember(request, userid, **kwargs)

    def forget(self, request, **kwargs):
        return self.authtkt.forget(request, **kwargs)


def login(request, host, username, password, realm):
    """Log into server and put credentials in session on success only.

    :raises LdbError: If the login failed or host is incorrect
    """
    samdb = connect_samdb(host, username, password, realm)

    if user_sid := samdb.connecting_user_sid:
        request.session["samba.username"] = username
        request.session["samba.password"] = password
        request.session["samba.host"] = host
        request.session["samba.realm"] = realm
        return remember(request, user_sid)


def logout(request):
    """Log the user out and delete credentials from the session."""
    # Delete session keys but always expect some could be missing.
    if "samba.username" in request.session:
        del request.session["samba.username"]
    if "samba.password" in request.session:
        del request.session["samba.password"]
    if "samba.host" in request.session:
        del request.session["samba.host"]
    if "samba.realm" in request.session:
        del request.session["samba.realm"]

    return forget(request)
