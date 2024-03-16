from pyramid.view import view_config

from sambal.resources import ContainerResource, Resource, RootFactory


def flatten(resource: Resource) -> dict:
    """Remove nested containers at the view level.

    This can't easily be done at the Resource level otherwise it stops
    traversal completely.

    Filter out children of containers to stop it returning nested containers.
    """
    if isinstance(resource, ContainerResource):
        return {k: obj for k, obj in resource.items() if not isinstance(obj, Resource)}

    return resource


@view_config(context=ContainerResource, permission="read", renderer="json")
@view_config(context=RootFactory, permission="read", renderer="json")
def container_view(context, request):
    """View for containers and the roof factory which is also a container.

    First of all filtering out anything but Resource takes out the keys that
    are on the container itself. These can be retrieved from the parent.

    Secondly, flatten removes any nested containers. Right now this is only
    an issue for the RootFactory, but it could also be in some containers.
    Without flatten it ends up returning endless nested data.

    This could otherwise make responses too big for larger domains.
    """
    return {k: flatten(obj) for k, obj in context.items() if isinstance(obj, Resource)}


@view_config(context=Resource, permission="read", renderer="json")
def resource_view(context, request):
    """View to produce JSON for non-container resources.

    This returns data on the current node and doesn't need to worry about
    children as there won't be any.
    """
    return context
