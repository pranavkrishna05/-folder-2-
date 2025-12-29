"""
Password reset model for representing reset token data.
"""

from datetime import datetime
from pydantic import BaseModel

class PasswordReset(BaseModel):
    token: str
    user_id: int
    expires_at: datetime