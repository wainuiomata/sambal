from typing import Optional

from ldb import LdbError
from samba.auth import system_session
from samba.credentials import Credentials
from samba.param import LoadParm
from samba.samdb import SamDB


def connect_samdb(username, password, host, realm=None) -> Optional[SamDB]:
    """Connect to Samba or Windows host and return SamDB on success."""
    if host and username and password:
        if host.startswith(("ldap://", "ldaps://")):
            url = host
        else:
            url = f"ldap://{host}"

        lp = LoadParm()
        lp.load_default()

        creds = Credentials()
        creds.set_username(username)
        creds.set_password(password)

        if realm:
            creds.set_realm(realm)

        try:
            return SamDB(
                url=url,
                session_info=system_session(),
                credentials=creds,
                lp=lp,
            )
        except LdbError:
            return None


def get_samdb(request) -> Optional[SamDB]:
    """Returns a SamDB connection to be used via the request.samdb property.

    :param request: Pyramid request object
    :return: SamDB or None if no credentials in session
    """
    # Fetch credentials out of the session after user logs in.
    # For this to be secure the session MUST be a backend session only.
    username = request.session.get("samba.username")
    password = request.session.get("samba.password")
    host = request.session.get("samba.host")
    realm = request.session.get("samba.realm")

    return connect_samdb(username, password, host, realm)
