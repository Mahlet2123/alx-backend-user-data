#!/usr/bin/env python3
""" basic_auth """
from api.v1.auth.auth import Auth


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
        if authorization_header is None or not isinstance(authorization_header, str) or not authorization_header.startswith('Basic '):
            return None
        else:
            value = authorization_header.split(" ")
            return value[1]
