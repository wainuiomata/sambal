from typing import Type

from samba.domain.models import Model

# A lookup table object_class to Resource class.
RESOURCES = {}


class ResourceMeta(type):
    """Resource metaclass automatically populates the RESOURCES lookup table.

    This lookup table is used by resource_for_model to find a resource for
    the given object class.
    """

    def __new__(mcls, name, bases, namespace, **kwargs):
        cls = super().__new__(mcls, name, bases, namespace, **kwargs)
        RESOURCES[cls.model.get_object_class()] = cls
        return cls


class Resource(dict, metaclass=ResourceMeta):
    """Resource base class represents the object class "top" or the base Model.

    Create specific resources for each Model subclass inheriting of Resource.
    """

    model = Model

    def __init__(self, request, obj):
        """The constructor for non-container objects.

        Container objects need to fetch the children as well, regular objects
        don't have to do this and are simply an update of the current object.
        """
        super().__init__()
        self.update(obj.as_dict())

    @staticmethod
    def resource_for_model(obj: Model) -> Type["Resource"]:
        """Traverse object hierarchy in reverse finding the closest Resource"""
        object_hierarchy = reversed(obj.object_class)

        for object_class in object_hierarchy:
            if resource := RESOURCES.get(object_class):
                return resource

        return Resource
