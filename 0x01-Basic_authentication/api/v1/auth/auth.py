#!/usr/bin/env python3
"""
Authentication module for the API
"""
import re
from typing import List,TypeVar
from flask import request


class Auth:
    """Class for the Auth module
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Returns the Path"""
        if path is not None and excluded_paths is not None:
            for excluded_path in map(lambda x: x.strip(),excluded_paths):
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
