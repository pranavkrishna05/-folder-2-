-----------------------------------------------
from typing import List, Optional
from backend.models.user import User
from backend.repositories.users.user_repository import UserRepository

class UserService:
    def __init__(self, repository: UserRepository) -> None:
        self.repository = repository
    
    def create_user(self, id: int, name: str, email: str, is_active: bool) -> User:
        user = User(id=id, name=name, email=email, is_active=is_active)
        self.repository.add_user(user)
        return user
    
    def get_user(self, user_id: int) -> Optional[User]:
        return self.repository.get_user_by_id(user_id)

    def get_all_users(self) -> List[User]:
        return self.repository.list_users()