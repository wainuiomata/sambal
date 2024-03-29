from samba.domain.models import Model


class TPMInformationObjectsContainer(Model):
    """TPM Devices container model."""

    @staticmethod
    def get_object_class():
        return "msTPM-InformationObjectsContainer"
