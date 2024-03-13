from ldb import SCOPE_ONELEVEL
from samba.netcmd.domain.models import Model

from .resource import Resource


class RootFactory(dict):
    model = Model

    def __init__(self, request):
        if request.samdb:
            qs = self.model.query(
                request.samdb,
                base_dn=request.samdb.get_root_basedn(),
                scope=SCOPE_ONELEVEL,
            )
            data = {obj.name: Resource(request, obj) for obj in qs if obj}
        else:
            data = {}

        super().__init__(**data)
