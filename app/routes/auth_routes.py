"""
Authentication-related API routes.
"""

from flask import Blueprint
from app.controllers.session_controller import session_blueprint

auth_blueprint = Blueprint("auth", __name__, url_prefix="/auth")

# Register blueprints
auth_blueprint.register_blueprint(session_blueprint)