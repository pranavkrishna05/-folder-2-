from flask import Blueprint, request, jsonify
from app.product_management.services.search_service import SearchService
import logging

search_bp = Blueprint('search', __name__, url_prefix='/api/v1/search')

logger = logging.getLogger(__name__)

@search_bp.route('/products', methods=['GET'])
def search_products():
    query = request.args.get('query', '')
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)

    try:
        results = SearchService.search_products(query, page, per_page)
        return jsonify(results), 200
    except Exception as e:
        logger.error(f'Error searching products: {e}')
        return jsonify({'error': str(e)}), 500
