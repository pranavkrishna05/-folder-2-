-----------------------------------------------
from typing import List, Optional
from backend.models.user import User

class UserRepository:
    def __init__(self) -> None:
        self.users: List[User] = []

    def add_user(self, user: User) -> None:
        self.users.append(user)
    
    def get_user_by_id(self, user_id: int) -> Optional[User]:
        for user in self.users:
            if user.id == user_id:
                return user
        return None
    
    def list_users(self) -> List[User]:
        return self.users