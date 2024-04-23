#!/usr/bin/env python3
"""Defines the User model for the database."""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    """Represents a user in the system."""

    __tablename__ = 'users'

    id: int = Column(Integer, primary_key=True)
    email: str = Column(String, nullable=False)
    hashed_password: str = Column(String, nullable=False)
    session_id: str = Column(String, nullable=True)
    reset_token: str = Column(String, nullable=True)

    def __init__(self, email: str, hashed_password: str,
                session_id: str = None, reset_token: str = None):
        self.email = email
        self.hashed_password = hashed_password
        self.session_id = session_id
        self.reset_token = reset_token

    def __repr__(self):
        return f"<User(id={self.id}, email={self.email},
            session_id={self.session_id}, reset_token={self.reset_token})>"
