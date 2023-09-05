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
        # Remove any trailing slash from the path before checking
        if path and not path.endswith('/'):
            path += '/'

        if not path or path not in excluded_paths:
            return True
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
