from pyramid.view import view_config

from sambal.resources import Resource, RootFactory


@view_config(context=Resource, permission="read", renderer="json")
@view_config(context=RootFactory, permission="read", renderer="json")
def resource_view(context, request):
    """Temporary view to produce JSON for every node.

    For this to work a custom JSON encoder is used to deal with the
    various objects that aren't JSON encode-able out of the box.
    """
    return context
