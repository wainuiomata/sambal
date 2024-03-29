from samba.domain.models import OrganizationalPerson

from sambal.models import OrganizationalUnit

from .container import ContainerResource
from .resource import Resource


class OrganizationalPersonResource(Resource):
    model = OrganizationalPerson


class OrganizationalUnitResource(ContainerResource):
    model = OrganizationalUnit
