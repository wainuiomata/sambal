from samba.domain.models.fields import BinaryField, NtTimeField

from .leaf import Leaf


class Secret(Leaf):
    """Secret model."""

    current_value = BinaryField("currentValue", hidden=True)
    last_set_time = NtTimeField("lastSetTime")
    prior_set_time = NtTimeField("priorSetTime")
    prior_value = BinaryField("priorValue", hidden=True)

    @staticmethod
    def get_object_class():
        return "secret"
