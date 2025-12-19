# user_repository.py
from backend.models.user import User
from backend.models import db

class UserRepository:
    def get_by_email(self, email):
        return User.query.filter_by(email=email).first()

    def save(self, user):
        db.session.add(user)
        db.session.commit()
