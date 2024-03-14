from ldb import SCOPE_ONELEVEL
from samba.domain.models import Container, Model

from .resource import Resource


class ContainerResource(Resource):
    model = Container

    def __init__(self, request, container):
        super().__init__(request, container)

        if request.samdb:
            queryset = Model.query(
                request.samdb,
                base_dn=container.dn,
                scope=SCOPE_ONELEVEL,
                polymorphic=True,
            )

            self["children"] = []
            for obj in queryset:
                if obj:
                    resource_class = self.resource_for_model(obj)
                    self["children"].append(resource_class(request, obj))
