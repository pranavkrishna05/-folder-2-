"""
Service for managing product deletion from the catalog.
"""

from db.database import Database

class ProductDeleteService:
    """
    Handles product deletion and admin validation logic.
    """
    
    ADMIN_SECRET = "super-secret-admin-token"  # Example admin token for validation purposes.

    def __init__(self):
        self.db = Database()

    def validate_admin(self, token: str) -> bool:
        """
        Validates if the provided token belongs to an authorized admin.
        """
        return token == self.ADMIN_SECRET

    def delete_product(self, product_id: int) -> bool:
        """
        Deletes the product if it exists.
        Returns True if the deletion was successful, False otherwise.
        """
        return self.db.delete_product(product_id)