#!/usr/bin/env python3
'''6. Basic auth'''
from api.v1.auth.auth import Auth
import base64
from typing import TypeVar
from models.user import User


class BasicAuth(Auth):
    '''BasicAuth that inherits from Auth'''
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        '''returns the Base64 part of the Authorization header'''
        if (not authorization_header
           or not isinstance(authorization_header, str)
           or authorization_header[0:6] != 'Basic '):
            return None
        return authorization_header[6:]

    def decode_base64_authorization_header(self,
                                           base64_auth_header: str) -> str:
        '''returns the decoded value of a Base64 string'''
        if (not base64_auth_header
           or not isinstance(base64_auth_header, str)):
            return None
        try:
            return base64.b64decode(base64_auth_header).decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(self, decoded_header: str) -> (str, str):
        '''returns the user email and password from
        the Base64 decoded value'''
        if (not decoded_header
           or not isinstance(decoded_header, str)
           or ':' not in decoded_header):
            return None, None
        index = decoded_header.index(':')
        return decoded_header[:index], decoded_header[index + 1:]

    def user_object_from_credentials(self,
                                     user_email: str,
                                     user_pwd: str) -> TypeVar('User'):
        ''' returns the User instance based on his email and password'''
        if (not user_email or not isinstance(user_email, str)
           or not user_pwd or not isinstance(user_pwd, str)):
            return None
        try:
            users = User.search({'email': user_email})
        except Exception:
            return None
        if len(users) <= 0:
            return None
        if users[0].is_valid_password(user_pwd):
            return users[0]
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        '''overloads Auth and retrieves the User instance for a request'''
        auth_heeader = self.authorization_header(request)
        b64 = self.extract_base64_authorization_header(auth_heeader)
        decoded = self.decode_base64_authorization_header(b64)
        email, password = self.extract_user_credentials(decoded)
        return self.user_object_from_credentials(email, password)
