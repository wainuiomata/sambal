from samba.domain.models import User

from .resource import Resource


class UserResource(Resource):
    model = User
