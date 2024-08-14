#!/usr/bin/env python3
"""0. User model"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    """SQLAlchemy model named User for a database table named users"""
    __tablename__ = 'users'
    id = Column('id', Integer, primary_key=True)
    email = Column('email', String(255), nullable=False)
    hashed_password = Column('hashed_password', String(255), nullable=False)
    session_id = Column('session_id', String(255))
    reset_token = Column('reset_token', String(255))
