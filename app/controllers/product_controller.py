"""
Controller layer for product management routes.
"""

from flask import Blueprint, jsonify, request
from app.services.product_service import ProductService

product_blueprint = Blueprint("product", __name__, url_prefix="/product")


@product_blueprint.route("/update/<int:product_id>", methods=["PUT"])
def update_product(product_id: int):
    """Endpoint to update product details."""
    data = request.get_json()
    price = data.get("price")
    description = data.get("description")

    try:
        updated_product = ProductService.update_product(product_id=product_id, price=price, description=description)
        return jsonify(updated_product), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400