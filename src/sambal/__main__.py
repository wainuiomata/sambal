from waitress import serve

from . import app, SETTINGS

serve(app, host=SETTINGS["sambal.host"], port=SETTINGS["sambal.port"])
