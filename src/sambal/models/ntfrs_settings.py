from samba.domain.models.fields import BinaryField, DnField

from .application_settings import ApplicationSettings


class NTFRSSettings(ApplicationSettings):
    """NTFRS File Replication Service settings model."""

    frs_extensions = BinaryField("fRSExtensions", hidden=True)
    managed_by = DnField("managedBy")

    @staticmethod
    def get_object_class():
        return "nTFRSSettings"
