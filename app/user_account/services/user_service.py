from app.user_account.infrastructure.repositories.user_repository import UserRepository
from app.user_account.domain.entities.user import User
from werkzeug.security import generate_password_hash

class UserService:
    @staticmethod
    def register_user(email: str, password: str) -> None:
        if UserRepository.get_user_by_email(email):
            raise ValueError('Email already registered')

        hashed_password = generate_password_hash(password)
        user = User(email=email, password=hashed_password)
        UserRepository.add_user(user)
