from pyramid.view import view_config

from sambal.resources import Resource, RootFactory


@view_config(context=RootFactory, permission="read", renderer="json")
def root_view(context, request):
    """View for the root node (RootFactory).

    This is the view for "/" or home. Only show toplevel keys, or it just
    ends up showing everything.
    """
    return {field: list(resource.keys()) for field, resource in context.items()}


@view_config(context=Resource, permission="read", renderer="json")
def resource_view(context, request):
    """Temporary view to produce JSON for every node.

    For this to work a custom JSON encoder is used to deal with the
    various objects that aren't JSON encode-able out of the box.
    """
    return context
