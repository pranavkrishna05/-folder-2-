from app.database import db
from app.user_account.domain.entities.user import User
import logging

logger = logging.getLogger(__name__)

class UserRepository:
    @staticmethod
    def find_by_email(email: str) -> User:
        return User.query.filter_by(email=email).first()

    @staticmethod
    def update_password(user_id: int, new_password: str) -> None:
        user = User.query.get(user_id)
        if user:
            user.set_password(new_password)
            db.session.commit()
