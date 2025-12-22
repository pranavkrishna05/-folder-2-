from flask import Blueprint, request, jsonify
from app.services.search_product_service import SearchProductService
from app.repositories.product_repository import ProductRepository

search_product_blueprint = Blueprint('search_product', __name__)
search_product_service = SearchProductService(ProductRepository())

@search_product_blueprint.route('/search', methods=['GET'])
def search_products():
    query = request.args.get('query', '')
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 10))
    
    if not query:
        return jsonify({"message": "Search query is required"}), 400
    
    result = search_product_service.search_products(query, page, per_page)
    return jsonify(result), 200