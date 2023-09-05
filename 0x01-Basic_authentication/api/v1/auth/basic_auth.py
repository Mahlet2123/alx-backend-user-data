#!/usr/bin/env python3
""" basic_auth """
from api.v1.auth.auth import Auth
import base64


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
