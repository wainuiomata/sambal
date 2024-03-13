from ldb import SCOPE_ONELEVEL
from samba.netcmd.domain.models import Model


class Resource(dict):
    model = Model

    def __init__(self, request, obj):
        if request.samdb:
            qs = self.model.query(request.samdb, base_dn=obj.dn, scope=SCOPE_ONELEVEL)
            data = {model.name: model.as_dict() for model in qs if model}
        else:
            data = {}

        super().__init__(**data)
