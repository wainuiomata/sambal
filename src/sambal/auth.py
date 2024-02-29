from typing import Optional

from samba.netcmd.domain.models import User


def get_authenticated_user(request) -> Optional[User]:
    """Returns the authenticated Samba User object."""
    return User.get(request.samdb, object_sid=request.samdb.connecting_user_sid)
