from typing import Optional
from app.models.user import User
from app import db

class UserRepository:
    """
    Repository class for interacting with the User model.
    """
    
    def find_by_email(self, email: str) -> Optional[User]:
        return User.query.filter_by(email=email).first()
    
    def save(self, user: User) -> None:
        db.session.add(user)
        db.session.commit()