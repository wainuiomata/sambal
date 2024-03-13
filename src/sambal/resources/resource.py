from samba.domain.models import Model

# A lookup table object_class to Resource.
RESOURCES = {}


class ResourceMeta(type):
    def __new__(mcls, name, bases, namespace, **kwargs):
        cls = super().__new__(mcls, name, bases, namespace, **kwargs)
        RESOURCES[cls.model.get_object_class()] = cls
        return cls


class Resource(dict, metaclass=ResourceMeta):
    model = Model

    def __init__(self, request, obj):
        super().__init__()
        self.update(obj.as_dict())

    @staticmethod
    def resource_for_model(model):
        return RESOURCES.get(model.get_object_class(), Resource)
