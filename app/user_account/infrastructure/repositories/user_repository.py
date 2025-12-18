from app.database import db
from app.user_account.domain.entities.user import User

class UserRepository:
    @staticmethod
    def add_user(email: str, password: str) -> None:
        new_user = User(email=email, password=password)
        db.session.add(new_user)
        db.session.commit()

    @staticmethod
    def find_by_email(email: str) -> User:
        return User.query.filter_by(email=email).first()
