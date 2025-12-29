"""
Profile model definition for user profile representation.
"""

from pydantic import BaseModel

class Profile(BaseModel):
    user_id: int
    first_name: str | None
    last_name: str | None
    email: str
    phone: str | None
    address: str | None
    preferences: dict | None
```