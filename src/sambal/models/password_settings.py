from samba.domain.models import Model


class PasswordSettingsContainer(Model):
    """PasswordSettingsContainer container model."""

    @staticmethod
    def get_object_class():
        return "msDS-PasswordSettingsContainer"
