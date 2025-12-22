from typing import Optional, Tuple
from datetime import datetime, timedelta
from app.models.user import User
from app.models.session import Session
from app.repositories.user_repository import UserRepository
from app.repositories.session_repository import SessionRepository
from werkzeug.security import check_password_hash
import secrets

class AuthService:
    """
    Service class for managing authentication operations.
    """
    
    def __init__(self, user_repository: UserRepository, session_repository: SessionRepository) -> None:
        self.user_repository = user_repository
        self.session_repository = session_repository
    
    def login_user(self, email: str, password: str) -> Tuple[str, datetime]:
        user = self.user_repository.find_by_email(email)
        if not user or not check_password_hash(user.password, password):
            raise ValueError("Invalid credentials")
        
        token = secrets.token_hex(64)
        expiration = datetime.utcnow() + timedelta(hours=1)
        session = Session(user_id=user.id, token=token, expired_at=expiration)
        
        self.session_repository.save(session)
        return token, expiration
    
    def logout_user(self, token: str) -> None:
        session = self.session_repository.find_by_token(token)
        if session:
            self.session_repository.delete(session)