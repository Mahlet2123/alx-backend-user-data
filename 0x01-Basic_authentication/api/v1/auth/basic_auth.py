#!/usr/bin/env python3
""" basic_auth """
from api.v1.auth.auth import Auth
import base64
from models.user import User
from typing import TypeVar


class BasicAuth(Auth):
    """ class BasicAuth that inherits from Auth
    """

    def extract_base64_authorization_header(
            self,
            authorization_header: str
            ) -> str:
        """
        returns the Base64 part of the Authorization header
        for a Basic Authentication
        """
        if (
            authorization_header is None
            or not isinstance(authorization_header, str)
            or not authorization_header.startswith("Basic ")
        ):
            return None
        else:
            value = authorization_header.split(" ")
            return value[1]

    def decode_base64_authorization_header(
            self,
            base64_authorization_header: str
            ) -> str:
        """
        returns the decoded value of a Base64 string
        base64_authorization_header
        """
        if (
            base64_authorization_header is None
            or not isinstance(base64_authorization_header, str)
        ):
            return None
        try:
            decoded_value = base64.b64decode(base64_authorization_header)
            return decoded_value.decode('utf-8')
        except base64.binascii.Error:
            return None

    def extract_user_credentials(
            self,
            decoded_base64_authorization_header: str
            ) -> (str, str):
        """
        returns the user email and password
        from the Base64 decoded value.
        """
        if (
            decoded_base64_authorization_header is None
            or not isinstance(decoded_base64_authorization_header, str)
            or ":" not in decoded_base64_authorization_header
        ):
            return (None, None)
        else:
            values = decoded_base64_authorization_header.split(":")
            return (values[0], values[1])

    def user_object_from_credentials(
            self,
            user_email: str,
            user_pwd: str
        ) -> TypeVar('User'):
        """
        returns the User instance based on his email and password.
        """
        if (
            not user_email
            or not isinstance(user_email, str)
            or not user_pwd
            or not isinstance(user_pwd, str)
        ):
            return None
        try:
            users = User.search({'email': user_email})
        except Exception:
            return None
        if len(users) <= 0:
            return None
        if users[0].is_valid_password(user_pwd):
            return users[0]
