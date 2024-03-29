from samba.domain import models
from samba.domain.models.fields import IntegerField


class OrganizationalUnit(models.OrganizationalUnit):
    """OrganizationalUnit contains additional fields not in Samba yet.

    This is an example where the original Samba model can be overridden.
    The resource must be set up to use this model over the Samba one.
    """

    country_code = IntegerField("countryCode")
