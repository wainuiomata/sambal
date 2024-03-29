from samba.domain.models import Model


class Leaf(Model):
    """Leaf structural modal."""

    @staticmethod
    def get_object_class():
        return "leaf"
