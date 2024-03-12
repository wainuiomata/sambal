from datetime import datetime
from decimal import Decimal
from enum import Enum

from ldb import Dn, MessageElement, Result
from pyramid.renderers import JSON
from pyramid.request import Request
from samba.dcerpc.security import descriptor


def includeme(config):
    """Configure the builtin json renderer to handle more data types."""
    json_renderer = JSON(indent=2, sort_keys=True)
    json_renderer.add_adapter(datetime, datetime_adapter)
    json_renderer.add_adapter(Decimal, decimal_adapter)
    json_renderer.add_adapter(Dn, dn_adapter)
    json_renderer.add_adapter(Enum, enum_adapter)
    json_renderer.add_adapter(Result, ldb_result_adapter)
    json_renderer.add_adapter(MessageElement, message_element_adapter)
    json_renderer.add_adapter(descriptor, security_descriptor_adapter)
    config.add_renderer("json", json_renderer)


def datetime_adapter(obj: datetime, request: Request):
    return obj.isoformat()


def decimal_adapter(obj: Decimal, request: Request):
    return str(obj)


def dn_adapter(obj: Dn, request: Request):
    return str(obj)


def enum_adapter(obj: Enum, request: Request):
    return obj.value


def ldb_result_adapter(obj: Result, request: Request):
    return obj.msgs


def message_element_adapter(obj: MessageElement, request: Request):
    return str(obj)


def security_descriptor_adapter(obj: descriptor, request: Request):
    return obj.as_sddl()
