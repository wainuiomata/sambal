from typing import Optional

from samba.auth import system_session
from samba.credentials import Credentials
from samba.param import LoadParm
from samba.samdb import SamDB


def connect_samdb(host, username, password, realm=None) -> SamDB:
    """Connect to Samba or Windows host and return SamDB on success.

    :param host: Host name or URL
    :param username: Account name
    :param password: Account password
    :param realm: Optional realm
    :raises LdbError: on failure, caller should handle error.
    """
    if host.startswith(("ldap://", "ldaps://")):
        url = host
    else:
        url = f"ldap://{host}"

    lp = LoadParm()
    lp.load_default()

    creds = Credentials()
    creds.guess(lp)
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


def get_samdb(request) -> Optional[SamDB]:
    """Returns a SamDB connection to be used via the request.samdb property.

    Fetch credentials out of the session after user has logged in.
    All keys except for realm must be present.

    For this to be secure the session MUST be a backend session only,
    with a password on Redis and a unique session secret different to the
    authtkt cookie secret.

    :param request: Pyramid request object
    :return: SamDB or None if no credentials in session
    :raises LdbError: On connection error or if the credentials no longer work
    """
    try:
        host = request.session["samba.host"]
        username = request.session["samba.username"]
        password = request.session["samba.password"]
        realm = request.session.get("samba.realm")
        return connect_samdb(host, username, password, realm)
    except KeyError:
        return None
