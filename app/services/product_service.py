"""
Product service: application layer for business logic.
"""

from app.repositories.product_repository import ProductRepository


class ProductService:
    """Service layer to handle product-related logic."""

    @staticmethod
    def update_product(product_id: int, price: float = None, description: str = None) -> dict:
        """Update an existing product's details."""
        product = ProductRepository.get_product_by_id(product_id)
        if not product:
            raise ValueError("Product not found")

        ProductRepository.update_product(product_id=product.id, price=price, description=description)
        return {
            "id": product.id,
            "name": product.name,
            "price": product.price,
            "description": product.description,
        }