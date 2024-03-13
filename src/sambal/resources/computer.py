from samba.domain.models import Computer

from .resource import Resource


class ComputerResource(Resource):
    model = Computer
