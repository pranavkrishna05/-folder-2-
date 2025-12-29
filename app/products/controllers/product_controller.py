"""
Product Controller handling product creation and retrieval in the inventory.
"""

from flask import request, jsonify, Blueprint
from products.services.product_service import ProductService

product_controller = Blueprint("product_controller", __name__)
product_service = ProductService()

@product_controller.route("/products", methods=["POST"])
def add_product():
    """
    Endpoint to add a new product to the inventory.
    """
    data = request.json
    name = data.get("name")
    price = data.get("price")
    description = data.get("description")
    category = data.get("category")

    if not name or not price or not description or not category:
        return jsonify({"error": "Name, price, description, and category are required"}), 400

    if price <= 0:
        return jsonify({"error": "Price must be a positive number"}), 400

    product = product_service.create_product(name, price, description, category)
    if product:
        return jsonify(product.dict()), 201

    return jsonify({"error": "Product name must be unique"}), 400

@product_controller.route("/products", methods=["GET"])
def get_products():
    """
    Endpoint to fetch all products in the inventory.
    """
    products = product_service.get_all_products()
    return jsonify([product.dict() for product in products]), 200

@product_controller.route("/products/<int:product_id>", methods=["GET"])
def get_product(product_id):
    """
    Endpoint to fetch a specific product by ID.
    """
    product = product_service.get_product_by_id(product_id)
    if product:
        return jsonify(product.dict()), 200

    return jsonify({"error": "Product not found"}), 404