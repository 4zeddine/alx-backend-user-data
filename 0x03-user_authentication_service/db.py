#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine, tuple_
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError

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
        """saves the user to the database"""
        try:
            create_user = User(email=email, hashed_password=hashed_password)
            self._session.add(create_user)
            self._session.commit()
        except Exception:
            self._session.rollback()
            create_user = None
        return create_user

    def find_user_by(self, **kwargs) -> User:
        """Returns the first row found in the users table"""
        user_fields, user_values = [], []
        for key, value in kwargs.items():
            if hasattr(User, key):
                user_attr = getattr(User, key)
                user_fields.append(user_attr)
                user_values.append(value)
            else:
                raise InvalidRequestError()
        output = tuple_(*user_fields).in_([tuple(user_values)])
        result = self._session.query(User).filter(output).first()
        if result is None:
            raise NoResultFound()
        return result

    def update_user(self, user_id: int, **kwargs) -> None:
        """locates the user to update"""
        if self.find_user_by(id=user_id) is None:
            return
        user_attr = {}
        for key, value in kwargs.items():
            if hasattr(User, key):
                user_attr[getattr(User, key)] = value
            else:
                raise ValueError()
        self._session.query(User).filter(User.id == user_id).update(
            user_attr,
            synchronize_session=False,
        )
        self._session.commit()
