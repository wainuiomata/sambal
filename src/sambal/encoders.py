import json
from datetime import datetime
from decimal import Decimal
from enum import Enum

from ldb import Dn, MessageElement, Result
from samba.dcerpc.security import descriptor


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
