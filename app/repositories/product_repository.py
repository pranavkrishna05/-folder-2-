"""
Repository layer for product data interactions, including support for soft deletion.
"""

from app.models.product import Product, db


class ProductRepository:
    """Provides Product model-related database functionality."""

    @staticmethod
    def get_product_by_id(product_id: int) -> Product | None:
        """Retrieve a product by its ID, excluding deleted products."""
        return Product.query.filter_by(id=product_id, is_deleted=False).first()

    @staticmethod
    def get_all_products() -> list[Product]:
        """Retrieve all non-deleted products."""
        return Product.query.filter_by(is_deleted=False).all()

    @staticmethod
    def delete_product(product_id: int) -> None:
        """Perform soft deletion on a product."""
        product = ProductRepository.get_product_by_id(product_id)
        if product:
            product.delete_product()
            db.session.commit()