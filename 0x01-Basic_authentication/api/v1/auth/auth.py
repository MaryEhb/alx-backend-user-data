#!/usr/bin/env python3
'''3. Auth class'''
from flask import request
from typing import List, TypeVar


class Auth:
    '''class to manage the API authentication'''

    def require_auth(self,
                     path: str,
                     excluded_paths: List[str]) -> bool:
        '''returns boolan'''
        if not path or not excluded_paths or len(excluded_paths) == 0:
            return True
        if path[-1] != '/':
            path += '/'
        return path not in excluded_paths

    def authorization_header(self, request=None) -> str:
        '''return none'''
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        '''return None'''
        return None
