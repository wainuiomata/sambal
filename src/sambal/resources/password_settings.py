from sambal.models import PasswordSettingsContainer

from .container import ContainerResource


class PasswordSettingsContainerResource(ContainerResource):
    model = PasswordSettingsContainer
