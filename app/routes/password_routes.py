"""
Password reset-related API routes.
"""

from flask import Blueprint
from app.controllers.password_reset_controller import password_reset_blueprint

password_routes = Blueprint("password_routes", __name__, url_prefix="/password")

# Register blueprints
password_routes.register_blueprint(password_reset_blueprint)