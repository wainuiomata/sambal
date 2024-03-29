from samba.domain.models import Model


class BuiltinDomain(Model):
    """BuiltinDomain container model."""

    @staticmethod
    def get_object_class():
        return "builtinDomain"
