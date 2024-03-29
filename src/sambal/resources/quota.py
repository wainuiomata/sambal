from sambal.models import QuotaContainer

from .container import ContainerResource


class QuotaContainerResource(ContainerResource):
    model = QuotaContainer
