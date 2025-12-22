from typing import Optional
from app.models.session import Session
from app import db

class SessionRepository:
    """
    Repository class for interacting with the Session model.
    """
    
    def find_by_token(self, token: str) -> Optional[Session]:
        return Session.query.filter_by(token=token).first()
    
    def save(self, session: Session) -> None:
        db.session.add(session)
        db.session.commit()
    
    def delete(self, session: Session) -> None:
        db.session.delete(session)
        db.session.commit()