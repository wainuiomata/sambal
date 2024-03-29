from samba.domain.models import Model
from samba.domain.models.fields import DnField, StringField


class ApplicationSettings(Model):
    """ApplicationSettings base model."""

    application_name = StringField("applicationName")
    notification_list = DnField("notificationList", many=True)
    settings = StringField("msDS-Settings")

    @staticmethod
    def get_object_class():
        return "applicationSettings"
