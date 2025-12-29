"""
Product Search Controller for handling search functionality in the product catalog.
"""

from flask import request, jsonify, Blueprint
from products.services.product_search_service import ProductSearchService

product_search_controller = Blueprint("product_search_controller", __name__)
product_search_service = ProductSearchService()

@product_search_controller.route("/products/search", methods=["GET"])
def search_products():
    """
    Endpoint to search products by name, category, or attributes.
    Returns paginated results.
    """
    query = request.args.get("query")
    page = int(request.args.get("page", 1))
    per_page = int(request.args.get("per_page", 10))

    if not query:
        return jsonify({"error": "Search query is required"}), 400

    results = product_search_service.search_products(query, page, per_page)
    return jsonify({"results": [result.dict() for result in results]}), 200