"""
Session model definition for session representation.
"""

from datetime import datetime
from pydantic import BaseModel

class Session(BaseModel):
    session_token: str
    user_id: int
    expires_at: datetime
```