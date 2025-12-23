"""
API routes for application entities.
"""

from flask import Blueprint
from app.controllers.user_controller import user_blueprint

api_blueprint = Blueprint("api", __name__, url_prefix="/api")

# Register blueprints
api_blueprint.register_blueprint(user_blueprint)