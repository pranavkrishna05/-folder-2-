"""
Product model definition for inventory representation.
"""

from pydantic import BaseModel

class Product(BaseModel):
    id: int | None
    name: str
    price: float
    description: str
    category: str
```