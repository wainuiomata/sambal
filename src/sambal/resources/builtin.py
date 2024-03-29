from sambal.models import BuiltinDomain

from .container import ContainerResource


class BuiltinDomainResource(ContainerResource):
    model = BuiltinDomain
