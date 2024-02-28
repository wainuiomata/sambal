from waitress import serve

from . import app

serve(app, host="127.0.0.1", port=8000)
