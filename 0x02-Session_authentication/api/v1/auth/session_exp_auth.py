#!/usr/bin/env python3
"""Module for session expiration
"""
import os
from flask import request
from .session_auth import SessionAuth
from datetime import datetime, timedelta


class SessionExpAuth(SessionAuth):
    """Session expiration Class"""
    def __init__(self) -> None:
        """Creates a new session expiration"""
        super().__init__()
        try:
            self.session_duration = int(os.getenv('SESSION_DURATION', '0'))
        except Exception:
            self.session_duration = 0

    def create_session(self, user_id=None):
        """Creates a session id"""
        sess_id = super().create_session(user_id)
        if type(sess_id) is not str:
            return None
        self.user_id_by_session_id[sess_id] = {
            'user_id': user_id,
            'created_at': datetime.now()
        }
        return sess_id

    def user_id_for_session_id(self, session_id=None):
        """Return user ID from session"""
        if session_id in self.user_id_by_session_id:
            dict_user = self.user_id_by_session_id[session_id]
            if self.session_duration <= 0:
                return dict_user['user_id']
            if 'created_at' not in dict_user:
                return None
            time_diff = dict_user['created_at'] + timedelta(
                seconds=self.session_duration)
            if time_diff < datetime.now():
                return None
            return dict_user['user_id']
