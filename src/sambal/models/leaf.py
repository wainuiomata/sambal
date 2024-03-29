from samba.domain.models import Model


class Leaf(Model):
    """Leaf structural model."""

    @staticmethod
    def get_object_class():
        return "leaf"
