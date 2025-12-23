"""
Category model definition.
"""

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String

db = SQLAlchemy()


class Category(db.Model):
    """Representation of product categories."""

    __tablename__ = "categories"

    id: int = Column(Integer, primary_key=True)
    name: str = Column(String(100), unique=True, nullable=False)