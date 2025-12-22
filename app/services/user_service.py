from typing import Optional
from app.models.user import User
from app.repositories.user_repository import UserRepository
from werkzeug.security import generate_password_hash

class UserService:
    """
    Service class for managing user operations.
    """
    
    def __init__(self, user_repository: UserRepository) -> None:
        self.user_repository = user_repository
    
    def register_user(self, email: str, password: str) -> Optional[User]:
        if self.user_repository.find_by_email(email):
            raise ValueError("Email must be unique")
        hashed_password = generate_password_hash(password)
        new_user = User(email=email, password=hashed_password)
        self.user_repository.save(new_user)
        return new_user