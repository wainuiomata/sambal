import json
import os

from pyramid.settings import asbool

# Pyramid settings are traditionally loaded via PasteDeploy ini file.
# With this project we went a different way with env vars.
SETTINGS = {
    "sambal.debug": asbool(os.getenv("SAMBAL_DEBUG", default=False)),
    "sambal.https": asbool(os.getenv("SAMBAL_HTTPS", default=False)),
    "sambal.hsts": asbool(os.getenv("SAMBAL_HSTS", default=False)),
    "auth.secret": os.getenv("SAMBAL_AUTH_SECRET"),
    "redis.sessions.url": os.getenv("SAMBAL_REDIS_URL"),
    "redis.sessions.secret": os.getenv("SAMBAL_SESSION_SECRET"),
    "redis.sessions.serialize": lambda s: json.dumps(s).encode("utf-8"),
    "redis.sessions.deserialize": lambda s: json.loads(s.decode("utf-8")),
    "redis.sessions.cookie_httponly": True,
}

# Only if https is used set cookie_secure.
SETTINGS["redis.sessions.cookie_secure"] = SETTINGS["sambal.https"]
