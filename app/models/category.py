"""
Category model definition, supporting hierarchical structure.
"""

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

db = SQLAlchemy()


class Category(db.Model):
    """Representation of product categories."""

    __tablename__ = "categories"

    id: int = Column(Integer, primary_key=True)
    name: str = Column(String(100), unique=True, nullable=False)
    parent_id: int = Column(Integer, ForeignKey("categories.id"), nullable=True)

    parent: "Category" = relationship("Category", remote_side=[id], backref="subcategories")

    def to_dict(self) -> dict:
        """Convert Category object to a dictionary."""
        return {
            "id": self.id,
            "name": self.name,
            "parent_id": self.parent_id,
            "subcategories": [subcategory.to_dict() for subcategory in self.subcategories],
        }