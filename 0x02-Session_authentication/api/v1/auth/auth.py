#!/usr/bin/env python3
'''3. Auth class'''
from flask import request
from typing import List, TypeVar
from os import environ


class Auth:
    '''class to manage the API authentication'''

    def require_auth(self,
                     path: str,
                     excluded_paths: List[str]) -> bool:
        '''Define which routes don't need authentication
        Return: True if the path is not in the list of strings
        excluded_paths'''
        if not path or not excluded_paths or len(excluded_paths) == 0:
            return True
        if path[-1] != '/':
            path += '/'
        return path not in excluded_paths

    def authorization_header(self, request=None) -> str:
        '''Request validation'''
        if not request:
            return None
        return request.headers.get('Authorization', None)

    def current_user(self, request=None) -> TypeVar('User'):
        '''return None'''
        return None

    def session_cookie(self, request=None):
        '''returns a cookie value from a request'''

        if not request:
            return None

        SESSION_NAME = environ.get('SESSION_NAME')
        if not SESSION_NAME:
            return None
        session_id = request.cookies.get(SESSION_NAME)
        return session_id
