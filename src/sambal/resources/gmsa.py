from samba.domain.models import GroupManagedServiceAccount

from .resource import Resource


class GroupManagedServiceAccountResource(Resource):
    model = GroupManagedServiceAccount
