"""Main entry point for Flask-launched service."""

from flask import render_template

from . import app
from . import api_routes
from . import www_routes

app.register_blueprint(api_routes.api)
app.register_blueprint(www_routes.www)
