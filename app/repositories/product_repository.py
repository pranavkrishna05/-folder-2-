"""
Repository layer for product data interactions, including search functionality.
"""

from app.models.product import Product, db
from sqlalchemy.orm import Query


class ProductRepository:
    """Provides Product model-related database functionality."""

    @staticmethod
    def search_products(
        keyword: str, category: str = None, page: int = 1, per_page: int = 10
    ) -> dict:
        """Search products based on keyword and category."""
        query: Query = Product.query.filter(
            Product.name.ilike(f"%{keyword}%") | Product.description.ilike(f"%{keyword}%")
        )
        
        if category:
            query = query.filter(Product.category_name.ilike(f"%{category}%"))
        
        paginated_results = query.paginate(page=page, per_page=per_page, error_out=False)
        return {
            "total": paginated_results.total,
            "pages": paginated_results.pages,
            "current_page": paginated_results.page,
            "products": [product.to_dict() for product in paginated_results.items],
        }