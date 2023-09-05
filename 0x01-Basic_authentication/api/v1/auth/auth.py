#!/usr/bin/env python3
""" auth module """
from flask import request
from typing import List, TypeVar


class Auth:
    """ Auth class """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Checks if authentication is required for the given path.

        Args:
            path (str): The path to check for authentication.
            excluded_paths (List[str]): List of paths that do not require authentication.

        Returns:
            bool: True if authentication is required, False otherwise.
        """
        # In a real implementation, you would check if the 'path' requires authentication.
        # For this example, we'll assume that authentication is always required.
        return False

    def authorization_header(self, request=None) -> str:
        """
        Gets the authorization header from the Flask request.

        Args:
            request (Request): The Flask request object.

        Returns:
            str: The authorization header value.
        """
        # In a real implementation, you would extract the authorization header from the request.
        # For this example, we'll return None.
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Gets the current user based on the Flask request.

        Args:
            request (Request): The Flask request object.

        Returns:
            TypeVar('User'): The current user object.
        """
        # In a real implementation, you would retrieve the current user based on the request.
        # For this example, we'll return None.
        return None
