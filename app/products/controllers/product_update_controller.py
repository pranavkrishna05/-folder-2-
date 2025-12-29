"""
Product Controller for handling updates to existing products in the inventory.
"""

from flask import request, jsonify, Blueprint
from products.services.product_update_service import ProductUpdateService

product_update_controller = Blueprint("product_update_controller", __name__)
product_update_service = ProductUpdateService()

@product_update_controller.route("/products/<int:product_id>", methods=["PUT"])
def update_product(product_id):
    """
    Endpoint to update existing product details in the inventory.
    """
    data = request.json
    name = data.get("name")
    price = data.get("price")
    description = data.get("description")
    category = data.get("category")
    admin_token = request.headers.get("Admin-Token")

    if not admin_token or not product_update_service.validate_admin(admin_token):
        return jsonify({"error": "Unauthorized access"}), 403

    if price is not None and (not isinstance(price, (int, float)) or price <= 0):
        return jsonify({"error": "Price must be a valid positive number"}), 400

    if description == "":
        return jsonify({"error": "Description cannot be removed"}), 400

    update_data = {
        key: value for key, value in {"name": name, "price": price, "description": description, "category": category}.items() if value is not None
    }

    updated_product = product_update_service.update_product(product_id, update_data)
    if updated_product:
        return jsonify(updated_product.dict()), 200

    return jsonify({"error": "Product not found or update failed"}), 404