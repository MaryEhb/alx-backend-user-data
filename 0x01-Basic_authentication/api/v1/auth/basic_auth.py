#!/usr/bin/env python3
'''6. Basic auth'''
from api.v1.auth.auth import Auth


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
