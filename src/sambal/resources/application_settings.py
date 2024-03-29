from sambal.models import ApplicationSettings

from .resource import Resource


class ApplicationSettingsResource(Resource):
    model = ApplicationSettings
