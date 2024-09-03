#!/usr/bin/env python3
"""
Basic Authentication module for the API
"""
import re
import base64
import binascii
from dataclasses import field
from nis import match
from typing import Tuple, TypeVar

from .auth import Auth
from models.user import User


class BasicAuth(Auth):
    """Basic Authentication class
    """
    def extract_base64_authorization_header(
            self,
            authorization_header: str
    ) -> str:
        """Returns the Base64 part of the Authorization header"""
        if type(authorization_header) == str:
            ptrn = r'Basic (?P<token>.+)'
            matching = re.fullmatch(ptrn, authorization_header.strip())
            if matching is not None:
                return matching.group('token')
        return None

    def decode_base64_authorization_header(
            self,
            base64_authorization_header: str
    ) -> str:
        """Decodes the Base64 part of the Authorization header"""
        if type(base64_authorization_header) == str:
            try:
                res = base64.b64decode(
                    base64_authorization_header,
                    validate=True,
                )
                return res.decode('utf-8')
            except (binascii.Error, UnicodeDecodeError):
                return None

    def extract_user_credentials(
            self,
            decoded_base64_authorization_header: str
    ) -> (str, str):
        """Extracts the user credentials"""
        if type(decoded_base64_authorization_header) == str:
            user_pattern = r'(?P<user>[^:]+)'
            password_pattern = r'(?P<password>.+)'
            ptrn = fr'{user_pattern}:{password_pattern}'
            matching = re.fullmatch(ptrn,
                                    decoded_base64_authorization_header.strip())
            if matching is not None:
                user = matching.group('user')
                passwrd = matching.group('password')
                return user, passwrd
        return None, None