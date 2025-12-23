"""
Product service: application layer for business logic.
"""

from app.repositories.product_repository import ProductRepository
from app.repositories.category_repository import CategoryRepository


class ProductService:
    """Service layer to handle product-related logic."""

    @staticmethod
    def create_product(name: str, price: float, description: str, category_name: str) -> dict:
        """Create a product and add it to the inventory."""
        category = CategoryRepository.get_all_categories()
        if not category:
            raise ValueError("Category not found")

        if ProductRepository.get_product_by_name(name):
            raise ValueError("Product name must be unique")

        product = ProductRepository.add_product(name=name, price=price, description=description, category_name=category_name)
        return {"id": product.id, "name": product.name, "price": product.price}