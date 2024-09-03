#!/usr/bin/env python3
"""
Basic Authentication module for the API
"""
import re
import base64
import binascii
from .auth import Auth
from models.user import User
from typing import Tuple, TypeVar


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
            matching = re.fullmatch(
                ptrn,
                decoded_base64_authorization_header.strip())
            if matching is not None:
                user = matching.group('user')
                passwrd = matching.group('password')
                return user, passwrd
        return None, None

    def user_object_from_credentials(
            self,
            user_email: str,
            user_pwd: str
    ) -> TypeVar('User'):
        """Gets the user object from
        his credentials"""
        if type(user_email) == str and type(user_pwd):
            try:
                the_user = User.search({'email': user_email})
            except Exception:
                return None
            if len(the_user) <= 0:
                return None
            if the_user[0].is_valid_password(user_pwd):
                return the_user[0]
        return None

    def current_user(
            self,
            request=None
    ) -> TypeVar('User'):
        """Overloads Auth and retrieves
         the User instance for a request"""
        auth_header = self.authorization_header(request)
        auth_b64_token = self.extract_base64_authorization_header(auth_header)
        auth_decoded = self.decode_base64_authorization_header(auth_b64_token)
        email, passwrd = self.extract_user_credentials(auth_decoded)
        return self.user_object_from_credentials(email, passwrd)
