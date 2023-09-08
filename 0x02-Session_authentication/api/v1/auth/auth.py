#!/usr/bin/env python3
""" auth module """
import os
from flask import request
from typing import List, TypeVar
from fnmatch import fnmatch


class Auth:
    """ Auth class """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Checks if authentication is required for the given path.
        """
        if path is not None and excluded_paths is not None:
            for excluded_path in excluded_paths:
                if fnmatch(path, excluded_path):
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

    def session_cookie(self, request=None):

        """
        returns a cookie value from a request
        """
        if request is None:
            return None
        
        self.session_name = os.getenv('SESSION_NAME', '_my_session_id')
        return request.cookies.get(self.session_name)
