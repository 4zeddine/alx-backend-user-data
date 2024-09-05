#!/usr/bin/env python3
"""
Session Authentication module for the API
"""
from .auth import Auth
from models.user import User
from uuid import uuid4
from flask import request


class SessionAuth(Auth):
    """Class for Session Auth"""
    user_id_by_session_id = {}

    def create_session(
            self,
            user_id: str = None
    ) -> str:
        """Creats a new session"""
        if type(user_id) == str:
            sess_id = str(uuid4())
            self.user_id_by_session_id[sess_id] = user_id
            return sess_id

    def user_id_for_session_id(
            self,
            session_id: str = None
    ) -> str:
        """Gets the user id based on session"""
        if type(session_id) == str:
            return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """Returns user instance based on session"""
        return User.get(self.user_id_for_session_id(\
            self.session_cookie(request)))
