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
        if path is not None and excluded_paths is not None:
            if not path.endswith('/'):
                path += '/'
            if path in excluded_paths:
                return False

        if not path or not excluded_paths or path not in excluded_paths:
            return True

    def authorization_header(self, request=None) -> str:
        """
        Gets the authorization header from the Flask request.
        """
        if not request or 'Authorization' not in request.headers:
            return None
        return request.headers['Authorization']

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Gets the current user based on the Flask request.
        """
        return None
