import json
from datetime import datetime
from decimal import Decimal
from enum import Enum

from ldb import Dn, MessageElement, Result
from samba.dcerpc.security import descriptor


def includeme(config):
    """Configure the Jinja2 template environment.

    Register any custom template filters and custom tags here.
    """

    def setup_jinja2_env():
        """Configure Jinja2 tojson filter to use the custom JSONEncoder."""
        env = config.get_jinja2_environment()

        # Jinja2 cannot use adapters so use a custom JSONEncoder instead.
        env.policies["json.dumps_kwargs"].update(
            {
                "cls": JSONEncoder,
                "indent": 2,
                "sort_keys": True,
            }
        )

    config.action(None, setup_jinja2_env, order=999)


class JSONEncoder(json.JSONEncoder):
    """Custom JSON encoder to deal with special datatypes.

    This feels like repetition from renderers.py, but with pyramid_jinja2
    you can only replace the JSONEncoder, while with the Pyramid JSON
    renderer you add adapters instead.

    Trying to get the Pyramid JSON renderer to use a different encoder
    class leads to nothing but trouble.
    """

    def default(self, obj):
        if isinstance(obj, (Decimal, Dn, MessageElement)):
            return str(obj)
        elif isinstance(obj, Result):
            return obj.msgs
        elif isinstance(obj, Enum):
            return str(obj.value)
        elif isinstance(obj, datetime):
            return obj.isoformat()
        elif isinstance(obj, descriptor):
            return obj.as_sddl()
        elif getattr(obj, "__json__", None) and callable(obj.__json__):
            # The request can be retrieved by thread-local but only if needed.
            return obj.__json__(request=None)
        return super().default(obj)
