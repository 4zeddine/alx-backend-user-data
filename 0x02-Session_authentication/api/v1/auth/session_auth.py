#!/usr/bin/env python3
"""Session Authentication module for the API
"""
from .auth import Auth
from models.user import User
from uuid import uuid4
from flask import request, session


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
        req_cookie = self.session_cookie(request)
        user_id = self.user_id_for_session_id(req_cookie)
        return User.get(user_id)

    def destroy_session(self, request=None):
        """Destroys a session"""
        if request is None:
            return False
        session_req = self.session_cookie(request)
        if session_req is None:
            return False
        user_id = self.user_id_for_session_id(session_req)
        if user_id is None:
            return False
        if session_req in self.user_id_by_session_id:
            del self.user_id_by_session_id[session_req]
        return True
