#!/usr/bin/env python3
""" session_auth module """
from api.v1.auth.auth import Auth
import uuid


class SessionAuth(Auth):
    """
    class SessionAuth that inherits from Auth
    """
    user_id_by_session_id = {}

    def create_session(
            self,
            user_id: str = None
            ) -> str:
        """
        creates a Session ID for a user_id
        """
        if (
                user_id is None
                or not isinstance(user_id, str)
            ):
            return None
        else:
            session_id = uuid.uuid4()
            self.user_id_by_session_id[str(session_id)] = user_id
            return session_id


