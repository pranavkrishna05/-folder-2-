"""
Service logic for managing user profiles.
"""

from auth.models.profile_model import Profile
from db.database import Database

class ProfileService:
    """
    Handles the retrieval and updates for user profiles.
    """
    
    def __init__(self):
        self.db = Database()  # Database instance
    
    def get_profile(self, user_id: int) -> Profile | None:
        """
        Retrieves a user's profile from the database.
        """
        profile_data = self.db.get_user_profile(user_id)
        if profile_data:
            return Profile(**profile_data)
        return None

    def update_profile(self, user_id: int, update_data: dict) -> Profile | None:
        """
        Updates a user's profile in the database.
        """
        if self.db.update_user_profile(user_id, update_data):
            return self.get_profile(user_id)
        return None