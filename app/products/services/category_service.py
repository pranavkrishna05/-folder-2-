"""
Service for managing category functionality.
"""

from products.models.category_model import Category
from db.database import Database

class CategoryService:
    """
    Handles creation, retrieval, and logic for categories.
    """

    ADMIN_SECRET = "super-secret-admin-token"  # Example admin token for validation purposes.

    def __init__(self):
        self.db = Database()

    def validate_admin(self, token: str) -> bool:
        """
        Validates if the provided token belongs to an authorized admin.
        """
        return token == self.ADMIN_SECRET

    def create_category(self, name: str, parent_id: int | None) -> Category | None:
        """
        Creates a category if no other category exists with the same name.
        """
        existing_category = self.db.get_category_by_name(name)
        if existing_category:
            return None

        category_data = {"name": name, "parent_id": parent_id}
        category_id = self.db.insert_category(category_data)
        return Category(id=category_id, **category_data)

    def get_all_categories(self) -> list[Category]:
        """
        Retrieves all categories from the database.
        """
        category_records = self.db.get_all_categories()
        return [Category(**record) for record in category_records]