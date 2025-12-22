from typing import Optional
from app.models.user import User
from app.repositories.user_repository import UserRepository

class ProfileService:
    """
    Service class for managing user profile operations.
    """
    
    def __init__(self, user_repository: UserRepository) -> None:
        self.user_repository = user_repository
    
    def update_profile(self, user_id: int, email: Optional[str] = None, password: Optional[str] = None) -> User:
        user = self.user_repository.find_by_id(user_id)
        if not user:
            raise ValueError("User not found")
        if email:
            user.email = email
        if password:
            user.password = password  # Assume password hasher is applied here
        self.user_repository.save(user)
        return user