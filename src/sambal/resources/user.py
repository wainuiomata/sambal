from samba.netcmd.domain.models import User

from .base import Resource


class UserResource(Resource):
    model = User
