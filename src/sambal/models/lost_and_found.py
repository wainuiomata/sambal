from samba.domain.models import Model


class LostAndFound(Model):
    """Default container for orphaned objects."""

    @staticmethod
    def get_object_class():
        return "lostAndFound"
