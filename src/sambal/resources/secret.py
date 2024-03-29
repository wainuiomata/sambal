from sambal.models import Secret

from .resource import Resource


class SecretResource(Resource):
    model = Secret
