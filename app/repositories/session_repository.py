"""
Repository layer for session data interactions.
"""

from datetime import datetime
from app.models.session import Session, db


class SessionRepository:
    """Provides Session model-related database functionality."""

    @staticmethod
    def create_session(user_id: int, session_token: str) -> Session:
        """Create and store a new session in the database."""
        new_session = Session(user_id=user_id, session_token=session_token)
        db.session.add(new_session)
        db.session.commit()
        return new_session

    @staticmethod
    def get_session_by_token(session_token: str) -> Session | None:
        """Retrieve a session by its token."""
        return Session.query.filter_by(session_token=session_token).first()

    @staticmethod
    def update_last_activity(session_id: int) -> None:
        """Update the last activity of a session."""
        session = Session.query.get(session_id)
        if session:
            session.last_activity_at = datetime.utcnow()
            db.session.commit()

    @staticmethod
    def delete_session(session_id: int) -> None:
        """Delete a session by its ID."""
        session = Session.query.get(session_id)
        if session:
            db.session.delete(session)
            db.session.commit()