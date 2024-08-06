#!/usr/bin/env python3
'''6. Basic auth'''
from api.v1.auth.auth import Auth
import base64


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
