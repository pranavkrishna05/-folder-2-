"""
Session service: application layer for session management.
"""

import secrets
from app.repositories.session_repository import SessionRepository
from app.repositories.user_repository import UserRepository
from app.models.session import Session


class SessionService:
    """Service layer to handle session-related logic."""

    @staticmethod
    def login_user(email: str, password: str) -> dict:
        """Authenticate user and create a new session."""
        user = UserRepository.get_user_by_email(email)
        if not user or not user.check_password(password):
            raise ValueError("Invalid email or password")

        # Invalidate old sessions for this user
        existing_sessions = Session.query.filter_by(user_id=user.id).all()
        for session in existing_sessions:
            SessionRepository.delete_session(session.id)

        # Create new session
        session_token = secrets.token_hex(32)
        new_session = SessionRepository.create_session(user_id=user.id, session_token=session_token)
        return {"user_id": new_session.user_id, "session_token": new_session.session_token}

    @staticmethod
    def validate_session(session_token: str) -> bool:
        """Validate the session based on activity timeout."""
        session = SessionRepository.get_session_by_token(session_token)
        if not session or not session.is_active():
            return False
        SessionRepository.update_last_activity(session.id)
        return True