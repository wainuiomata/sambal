import json
import os

from pyramid.settings import asbool
from redis.connection import parse_url

# Read environment variables then do some sanity checks.
DEBUG = asbool(os.getenv("SAMBAL_DEBUG", default=False))
USE_HTTPS = asbool(os.getenv("SAMBAL_HTTPS", default=False))
USE_HSTS = asbool(os.getenv("SAMBAL_HSTS", default=False))
REDIS_URL = os.getenv("SAMBAL_REDIS_URL")
SESSION_SECRET = os.getenv("SAMBAL_SESSION_SECRET")
AUTH_SECRET = os.getenv("SAMBAL_AUTH_SECRET")

if REDIS_URL is None:
    raise ValueError("Missing SAMBAL_REDIS_URL environment variable")

if "password" not in parse_url(REDIS_URL):
    raise ValueError("Missing password in SAMBAL_REDIS_URL, please add one")

if SESSION_SECRET is None:
    raise ValueError("Missing SAMBAL_SESSION_SECRET environment variable")

if AUTH_SECRET is None:
    raise ValueError("Missing SAMBAL_AUTH_SECRET environment variable")

if SESSION_SECRET == AUTH_SECRET:
    raise ValueError(
        "Use different values for SAMBAL_AUTH_SECRET and SAMBAL_SESSION_SECRET"
    )

# Pyramid settings are traditionally loaded via PasteDeploy ini file.
# With this project we went a different way with env vars.
SETTINGS = {
    "sambal.debug": DEBUG,
    "sambal.https": USE_HTTPS,
    "sambal.hsts": USE_HSTS,
    "auth.secret": AUTH_SECRET,
    "redis.sessions.url": REDIS_URL,
    "redis.sessions.secret": SESSION_SECRET,
    "redis.sessions.serialize": lambda s: json.dumps(s).encode("utf-8"),
    "redis.sessions.deserialize": lambda s: json.loads(s.decode("utf-8")),
    "redis.sessions.cookie_samesite": "Strict",
    "redis.sessions.cookie_httponly": True,
    "redis.sessions.cookie_secure": USE_HTTPS,
}
