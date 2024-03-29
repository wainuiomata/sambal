from ldb import SCOPE_ONELEVEL
from samba.domain.models import Model

from .resource import Resource


class RootFactory(dict):
    model = Model

    def __init__(self, request):
        super().__init__()

        if request.samdb:
            queryset = self.model.query(
                request.samdb,
                base_dn=request.samdb.get_root_basedn(),
                scope=SCOPE_ONELEVEL,
                polymorphic=True,
            )

            for obj in queryset:
                if obj:
                    resource_class = Resource.resource_for_model(obj)
                    self[obj.name] = resource_class(request, obj)
