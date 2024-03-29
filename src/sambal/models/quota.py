from samba.domain.models import Model
from samba.domain.models.fields import IntegerField, StringField


class QuotaContainer(Model):
    """QuotaContainer container model."""

    default_quota = IntegerField("msDS-DefaultQuota")
    tombstone_quota_factor = IntegerField("msDS-TombstoneQuotaFactor")
    quota_effective = IntegerField("msDS-QuotaEffective", readonly=True)
    quota_used = IntegerField("msDS-QuotaUsed", readonly=True)
    top_quota_usage = StringField("msDS-TopQuotaUsage", many=True)

    @staticmethod
    def get_object_class():
        return "msDS-QuotaContainer"
