"""
User model definition for database interaction.
"""

from datetime import datetime
from pydantic import BaseModel, EmailStr

class User(BaseModel):
    id: int | None
    email: EmailStr
    password_hash: str
    created_at: datetime | None
    updated_at: datetime | None