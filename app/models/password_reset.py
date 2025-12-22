from app import db
from datetime import datetime, timedelta

class PasswordReset(db.Model):
    """
    PasswordReset model for storing password reset tokens.
    """
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    token = db.Column(db.String(128), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    expired_at = db.Column(db.DateTime, nullable=False)
    used = db.Column(db.Boolean, default=False, nullable=False)

    def __repr__(self):
        return f"PasswordReset('{self.user_id}', '{self.token}', '{self.expired_at}', 'Used: {self.used}')"