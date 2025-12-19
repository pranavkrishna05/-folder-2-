
from flask import Blueprint

categories_bp = Blueprint('categories', __name__)

@categories_bp.route('/categories')
def categories():
    return 'Categories Page'
