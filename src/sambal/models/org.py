from samba.domain.models.fields import IntegerField, StringField
from samba.domain.models import Model


class OrganizationalUnit(Model):
    """OrganizationalUnit container model.

    This model exists in upstream Samba but many of the fields are missing.
    The model is declared again here which overrides the original.
    """

    ou = StringField("ou")
    country_code = IntegerField("countryCode")

    def __str__(self):
        return str(self.ou)

    @staticmethod
    def get_object_class():
        return "organizationalUnit"
