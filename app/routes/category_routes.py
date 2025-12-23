"""
Category-related API routes.
"""

from flask import Blueprint
from app.controllers.category_controller import category_blueprint

category_routes = Blueprint("category_routes", __name__, url_prefix="/categories")

# Register blueprints
category_routes.register_blueprint(category_blueprint)