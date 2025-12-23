"""
Controller layer for shopping cart management routes, including quantity modification.
"""

from flask import Blueprint, jsonify, request
from app.services.cart_service import CartService

cart_blueprint = Blueprint("cart", __name__, url_prefix="/cart")


@cart_blueprint.route("/modify-quantity", methods=["PUT"])
def modify_cart_item_quantity():
    """Endpoint to modify the quantity of an item in the shopping cart."""
    data = request.get_json()
    cart_id = data.get("cart_id")
    item_id = data.get("item_id")
    new_quantity = data.get("new_quantity")

    if not cart_id or not item_id or new_quantity is None:
        return jsonify({"error": "Cart ID, Item ID, and new quantity are required"}), 400

    try:
        updated_cart = CartService.modify_item_quantity(cart_id=cart_id, item_id=item_id, new_quantity=new_quantity)
        return jsonify(updated_cart), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400