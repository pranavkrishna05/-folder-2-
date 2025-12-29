"""
Service logic for user registration and authentication.
"""

import bcrypt

from auth.models.user_model import User
from db.database import Database

class UserService:
    def __init__(self, database: Database):
        self.db = database

    def register_user(self, email: str, password: str) -> User:
        hashed_password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
        user = User(email=email, password_hash=hashed_password)
        self.db.create_user(user)
        return user

    def authenticate_user(self, email: str, password: str) -> bool:
        user = self.db.get_user_by_email(email)
        return bcrypt.checkpw(password.encode("utf-8"), user.password_hash.encode("utf-8"))