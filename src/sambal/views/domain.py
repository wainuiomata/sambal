from pyramid.view import view_config

from sambal.resources import ContainerResource, Resource, RootFactory


def flatten(resource: Resource) -> dict:
    """Remove nested containers at the view level.

    This can't easily be done at the Resource level otherwise it stops
    traversal completely.
    """
    # Filter children of containers to stop it returning infinite nested data.
    if isinstance(resource, ContainerResource):
        return {k: obj for k, obj in resource.items() if not isinstance(obj, Resource)}

    return resource


@view_config(context=Resource, permission="read", renderer="json")
@view_config(context=RootFactory, permission="read", renderer="json")
def resource_view(context, request):
    """Temporary view to produce JSON for every node.

    For this to work a custom JSON encoder is used to deal with the
    various objects that aren't JSON encode-able out of the box.
    """
    return {k: flatten(obj) for k, obj in context.items() if isinstance(obj, Resource)}
