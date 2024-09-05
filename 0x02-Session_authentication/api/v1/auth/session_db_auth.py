#!/usr/bin/env python3
"""Module for session database
"""
from flask import request
from datetime import datetime, timedelta
from models.user_session import UserSession
from .session_exp_auth import SessionExpAuth


class SessionDBAuth(SessionExpAuth):
    """Database session auth Class"""

    def create_session(self, user_id=None) -> str:
        """initializes and stores a users session id."""
        sess_id = super().create_session(user_id)
        if type(sess_id) is str:
            input_args = {
                'user_id': user_id,
                'session_id': sess_id,
            }
            get_session = UserSession(**input_args)
            get_session.save()
            return sess_id

    def user_id_for_session_id(self, session_id=None):
        """Returns user id from a session"""
        try:
            req_session = UserSession.search({'session_id': session_id})
        except Exception:
            return None
        if len(req_session) <= 0:
            return None
        time_diff = req_session[0].created_at + timedelta(
            seconds=self.session_duration)
        if time_diff < datetime.now():
            return None
        return req_session[0].user_id

    def destroy_session(self, request=None) -> bool:
        """Deletes a session"""
        sess_id = self.session_cookie(request)
        try:
            req_session = UserSession.search({'session_id': sess_id})
        except Exception:
            return False
        if len(req_session) <= 0:
            return False
        req_session[0].remove()
        return True