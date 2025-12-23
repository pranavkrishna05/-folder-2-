"""
Product service: application layer for business logic regarding deletion.
"""

from app.repositories.product_repository import ProductRepository


class ProductService:
    """Service layer to handle product deletion."""

    @staticmethod
    def delete_product(product_id: int) -> None:
        """Delete a product from the catalog."""
        product = ProductRepository.get_product_by_id(product_id)
        if not product:
            raise ValueError("Product not found or already deleted")

        ProductRepository.delete_product(product_id=product.id)