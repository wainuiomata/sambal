from ldb import SCOPE_ONELEVEL
from samba.netcmd.domain.models import Model

from .base import Resource


class RootFactory(dict):
    model = Model

    def __init__(self, request):
        if request.samdb:
            qs = self.model.query(request.samdb, scope=SCOPE_ONELEVEL)
            data = {obj.name: Resource(request, obj) for obj in qs if obj}
        else:
            data = {}

        super().__init__(**data)
