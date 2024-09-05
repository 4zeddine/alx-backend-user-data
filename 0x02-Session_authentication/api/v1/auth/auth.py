#!/usr/bin/env python3
"""Authentication module for the API
"""
import os
import re
from flask import request
from typing import List, TypeVar


class Auth:
    """Class for the Auth module
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Returns the Path"""
        if path is not None and excluded_paths is not None:
            for excluded_path in map(lambda x: x.strip(), excluded_paths):
                pattern = ''
                if excluded_path[-1] == '*':
                    pattern = '{}.*'.format(excluded_path[0:-1])
                elif excluded_path[-1] == '/':
                    pattern = '{}/*'.format(excluded_path[0:-1])
                else:
                    pattern = '{}/*'.format(excluded_path)
                if re.match(pattern, path):
                    return False
        return True

    def authorization_header(self, request=None) -> str:
        """Returns the authorization header field"""
        if request is not None:
            return request.headers.get('Authorization', None)
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Returns the current user"""
        return None

    def session_cookie(self, request=None):
        """Returns a cookie from a request"""
        if request is not None:
            name_of_cookie = os.getenv('SESSION_NAME')
            return request.cookies.get(name_of_cookie)
