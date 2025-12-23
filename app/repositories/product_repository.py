"""
Repository layer for product data interactions, ensuring category association.
"""

from app.models.product import Product, db


class ProductRepository:
    """Provides Product model-related database functionality."""

    @staticmethod
    def add_product(name: str, price: float, description: str, category_id: int) -> Product:
        """Add a new product and ensure it is linked to a category."""
        product = Product(name=name, price=price, description=description, category_id=category_id)
        db.session.add(product)
        db.session.commit()
        return product

    @staticmethod
    def get_product_by_id(product_id: int) -> Product | None:
        """Retrieve product by its ID."""
        return Product.query.get(product_id)