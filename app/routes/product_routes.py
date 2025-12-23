"""
Product-related API routes, including the delete functionality.
"""

from flask import Blueprint
from app.controllers.product_controller import product_blueprint

product_routes = Blueprint("product_routes", __name__, url_prefix="/products")

# Register blueprints
product_routes.register_blueprint(product_blueprint)