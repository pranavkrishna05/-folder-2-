"""
Service for managing updates to existing products.
"""

from products.models.product_model import Product
from db.database import Database

class ProductUpdateService:
    """
    Handles product updates and authorization logic.
    """
    
    ADMIN_SECRET = "super-secret-admin-token"  # Example admin token for validation purposes.

    def __init__(self):
        self.db = Database()

    def validate_admin(self, token: str) -> bool:
        """
        Validates if the provided token is authorized for admin access.
        """
        return token == self.ADMIN_SECRET

    def update_product(self, product_id: int, update_data: dict) -> Product | None:
        """
        Updates the product details if the product exists.
        """
        if self.db.update_product(product_id, update_data):
            updated_product_data = self.db.get_product_by_id(product_id)
            return Product(**updated_product_data)
        return None