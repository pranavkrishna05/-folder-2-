"""
Search-related API routes.
"""

from flask import Blueprint
from app.controllers.search_controller import search_blueprint

search_routes = Blueprint("search_routes", __name__, url_prefix="/products")

# Register blueprints
search_routes.register_blueprint(search_blueprint)