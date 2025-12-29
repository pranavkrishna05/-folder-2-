"""
Category model definition for representing categories.
"""

from pydantic import BaseModel

class Category(BaseModel):
    id: int | None
    name: str
    parent_id: int | None
```