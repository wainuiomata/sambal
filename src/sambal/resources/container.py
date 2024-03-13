from ldb import SCOPE_ONELEVEL
from samba.domain.models import Container

from .resource import Resource


class ContainerResource(Resource):
    model = Container

    def __init__(self, request, container):
        super().__init__(request, container)

        if request.samdb:
            queryset = self.model.query(
                request.samdb,
                base_dn=container.dn,
                scope=SCOPE_ONELEVEL,
                polymorphic=True,
            )

            for obj in queryset:
                if obj:
                    resource_class = self.resource_for_model(obj)
                    self[obj.name] = resource_class(request, obj)
