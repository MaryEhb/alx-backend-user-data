#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine, tuple_
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound

from user import Base, User


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """save the user to the database"""
        try:
            user = User(email=email, hashed_password=hashed_password)
            self._session.add(user)
            self._session.commit()
        except Exception:
            session.rollback()
            return None
        return user

    def find_user_by(self, **kwargs) -> User:
        """takes in arbitrary keyword arguments andreturns the first
        row found in the users table as filtered by the method’s
        input arguments."""

        atts, vals = [], []
        for att, val in kwargs.items():
            if not hasattr(User, att):
                raise InvalidRequestError()
            atts.append(getattr(User, att))
            vals.append(val)

        filter_tuple = tuple_(*atts).in_([tuple(vals)])
        user = self._session.query(User).filter(filter_tuple).first()
        if not user:
            raise NoResultFound()
        return user

    def update_user(self, user_id: int, **kwargs) -> None:
        """update user in db"""
        user = self.find_user_by(id=user_id)
        for att, val in kwargs.items():
            if not hasattr(User, att):
                raise ValueError
            setattr(user, att, val)
        self._session.commit()
