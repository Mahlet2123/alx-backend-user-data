#!/usr/bin/env python3
""" auth module """
from flask import request
from typing import List, TypeVar


class Auth:
    """ Auth class """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Checks if authentication is required for the given path.
        """
        return False

    def authorization_header(self, request=None) -> str:
        """
        Gets the authorization header from the Flask request.
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Gets the current user based on the Flask request.
        """
        return None
