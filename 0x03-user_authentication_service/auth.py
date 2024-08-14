#!/usr/bin/env python3
"""auth module"""

import bcrypt


def _hash_password(password: str) -> bytes:
    """takes in a password string and returns salted hash bytes"""
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())
