from typing import Optional
from app.models.password_reset import PasswordReset
from app import db

class PasswordResetRepository:
    """
    Repository class for interacting with the PasswordReset model.
    """
    
    def find_by_token(self, token: str) -> Optional[PasswordReset]:
        return PasswordReset.query.filter_by(token=token).first()
    
    def save(self, reset_token: PasswordReset) -> None:
        db.session.add(reset_token)
        db.session.commit()
    
    def mark_as_used(self, reset_token: PasswordReset) -> None:
        reset_token.used = True
        db.session.commit()