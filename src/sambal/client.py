from typing import Optional

from samba.auth import system_session
from samba.credentials import Credentials
from samba.param import LoadParm
from samba.samdb import SamDB


def get_samdb(request) -> Optional[SamDB]:
    """Returns a SamDB connection to be used via the request.samdb property.

    :param request: Pyramid request object
    :return: SamDB or None if no credentials in session
    """
    # Fetch credentials out of the session after user logs in.
    # For this to be secure the session MUST be a backend session only.
    host = request.session.get("samba.host")
    realm = request.session.get("samba.realm")
    username = request.session.get("samba.username")
    password = request.session.get("samba.password")

    # The host username and password are required, realm is optional.
    # Needs to be double-checked if this is correct.
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

        return SamDB(
            url=url,
            session_info=system_session(),
            credentials=creds,
            lp=lp,
        )
