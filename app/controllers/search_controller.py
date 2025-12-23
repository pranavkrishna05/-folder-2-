"""
Controller layer for search functionality routes.
"""

from flask import Blueprint, jsonify, request
from app.services.search_service import SearchService

search_blueprint = Blueprint("search", __name__, url_prefix="/search")


@search_blueprint.route("/", methods=["GET"])
def search_products():
    """Endpoint to search for products."""
    keyword = request.args.get("keyword")
    category = request.args.get("category")
    page = request.args.get("page", 1, type=int)
    per_page = request.args.get("per_page", 10, type=int)

    if not keyword:
        return jsonify({"error": "Search keyword is required"}), 400

    try:
        search_results = SearchService.search(keyword=keyword, category=category, page=page, per_page=per_page)
        return jsonify(search_results), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400