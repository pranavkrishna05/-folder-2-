"""
Repository layer for product data interactions.
"""

from app.models.product import Product, db


class ProductRepository:
    """Provides Product model-related database functionality."""

    @staticmethod
    def get_product_by_id(product_id: int) -> Product | None:
        """Retrieve product by its ID."""
        return Product.query.get(product_id)

    @staticmethod
    def update_product(product_id: int, price: float = None, description: str = None) -> None:
        """Update an existing product."""
        product = ProductRepository.get_product_by_id(product_id)
        if product:
            product.update_product(price=price, description=description)
            db.session.commit()