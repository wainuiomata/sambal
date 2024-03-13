from samba.domain.models import Group

from .resource import Resource


class GroupResource(Resource):
    model = Group
