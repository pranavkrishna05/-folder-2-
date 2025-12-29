"""
Session management service for handling user sessions.
"""

from datetime import datetime, timedelta
import uuid

class SessionService:
    """
    Handles session creation, validation, and invalidation.
    """

    def __init__(self):
        self.sessions = {}  # A mock in-memory session store

    def create_session(self, user_id: int) -> str:
        """
        Creates and returns a session token for a valid user.
        """
        session_token = str(uuid.uuid4())
        expiration_time = datetime.now() + timedelta(hours=1)
        self.sessions[session_token] = {"user_id": user_id, "expires_at": expiration_time}
        return session_token

    def validate_session(self, session_token: str) -> bool:
        """
        Validates if the given session token is active.
        """
        session = self.sessions.get(session_token)
        if session and session["expires_at"] > datetime.now():
            return True
        return False

    def invalidate_session(self, session_token: str) -> bool:
        """
        Invalidates the provided session token.
        """
        if session_token in self.sessions:
            del self.sessions[session_token]
            return True
        return False