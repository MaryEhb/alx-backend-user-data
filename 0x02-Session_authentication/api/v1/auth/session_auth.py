#!/usr/bin/env python3
'''SessionAuth class'''
from api.v1.auth.auth import Auth
import uuid


class SessionAuth(Auth):
    '''session auth inhirits from auth'''
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        '''creates a Session ID for a user_id'''
        if not user_id or not isinstance(user_id, str):
            return None
        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        '''returns a User ID based on a Session ID'''
        if not session_id or not isinstance(session_id, str):
            return None
        return self.user_id_by_session_id.get(session_id)
