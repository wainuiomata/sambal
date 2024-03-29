from samba.domain.models import Model


class SecurityObject(Model):
    """SecurityObject model."""

    @staticmethod
    def get_object_class():
        return "securityObject"
