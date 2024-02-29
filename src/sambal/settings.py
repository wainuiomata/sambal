import json
import os

# Pyramid settings are traditionally loaded via PasteDeploy ini file.
# With this project we went a different way with env vars.
SETTINGS = {
    "redis.sessions.url": os.getenv("SAMBAL_REDIS_URL"),
    "redis.sessions.secret": os.getenv("SAMBAL_SESSION_SECRET"),
    "redis.sessions.serialize": lambda s: json.dumps(s).encode("utf-8"),
    "redis.sessions.deserialize": lambda s: json.loads(s.decode("utf-8")),
}
