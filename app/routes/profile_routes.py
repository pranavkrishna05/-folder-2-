"""
Profile-related API routes.
"""

from flask import Blueprint
from app.controllers.profile_controller import profile_blueprint

profile_routes = Blueprint("profile_routes", __name__, url_prefix="/profile_routes")

# Register blueprints
profile_routes.register_blueprint(profile_blueprint)