"""
Controller layer for product management routes.
"""

from flask import Blueprint, jsonify, request
from app.services.product_service import ProductService

product_blueprint = Blueprint("product", __name__, url_prefix="/product")


@product_blueprint.route("/add", methods=["POST"])
def add_product():
    """Endpoint to add products."""