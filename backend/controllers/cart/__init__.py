# __init__.py
from flask import Blueprint
from backend.controllers.cart.cart_management import AddToCartAPI, ViewCartAPI, RemoveFromCartAPI

cart_blueprint = Blueprint('cart', __name__)

# Register routes
cart_blueprint.add_url_rule('/add', view_func=AddToCartAPI.as_view('add_to_cart'))
cart_blueprint.add_url_rule('/view', view_func=ViewCartAPI.as_view('view_cart'))
cart_blueprint.add_url_rule('/remove/<int:item_id>', view_func=RemoveFromCartAPI.as_view('remove_from_cart'))
