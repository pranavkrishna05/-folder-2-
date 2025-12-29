"""
Service logic for managing products in the inventory.
"""

from products.models.product_model import Product
from db.database import Database

class ProductService:
    """
    Handles creation, retrieval, and validation for products.
    """

    def __init__(self):
        self.db = Database()  # Database instance

    def create_product(self, name: str, price: float, description: str, category: str) -> Product | None:
        """
        Creates a new product if the name is unique.
        """
        existing_product = self.db.get_product_by_name(name)
        if existing_product:
            return None

        product_data = {
            "name": name,
            "price": price,
            "description": description,
            "category": category
        }
        product_id = self.db.insert_product(product_data)
        return Product(id=product_id, **product_data)

    def get_all_products(self) -> list[Product]:
        """
        Retrieves all products in the inventory.
        """
        product_records = self.db.get_all_products()
        return [Product(**record) for record in product_records]

    def get_product_by_id(self, product_id: int) -> Product | None:
        """
        Retrieves a specific product using its ID.
        """
        product_data = self.db.get_product_by_id(product_id)
        if product_data:
            return Product(**product_data)
        return None