from app.database import db
from app.user_account.domain.entities.user import User
import logging

logger = logging.getLogger(__name__)

class UserRepository:
    @staticmethod
    def find_by_id(user_id: int) -> User:
        return User.query.get(user_id)

    @staticmethod
    def save(user: User) -> None:
        db.session.commit()
