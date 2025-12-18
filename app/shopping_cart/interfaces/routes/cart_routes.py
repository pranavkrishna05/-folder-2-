from flask import Blueprint, request, jsonify, g
from app.shopping_cart.services.cart_service import CartService
import logging

cart_bp = Blueprint('cart', __name__, url_prefix='/api/v1/cart')
logger = logging.getLogger(__name__)

@cart_bp.route('/<int:product_id>', methods=['DELETE'])
def remove_product_from_cart(product_id):
    if not g.user:
        return jsonify({'error': 'User must be logged in'}), 403
    try:
        CartService.remove_product_from_cart(g.user.id, product_id)
        return jsonify({'message': 'Product removed from cart successfully'}), 200
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        logger.error(f'Error removing product from cart: {e}')
        return jsonify({'error': 'An unexpected error occurred'}), 500
