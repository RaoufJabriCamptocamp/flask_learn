"""Module Models."""
# Disable all the no-member violations in this function
# pylint: disable=no-member
from sqlalchemy import Column, Integer, String
from flaskr.db import Base


class User(Base):
    """User model"""

    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    email = Column(String(120), unique=True)

    def __init__(self, name=None, email=None):
        self.name = name
        self.email = email

    def __repr__(self):
        return f"<User {self.name!r}>"
