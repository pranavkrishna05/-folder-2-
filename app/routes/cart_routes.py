"""
Shopping cart-related API routes.
"""

from flask import Blueprint
from app.controllers.cart_controller import cart_blueprint

cart_routes = Blueprint("cart_routes", __name__, url_prefix="/shopping-cart")

# Register blueprints
cart_routes.register_blueprint(cart_blueprint)