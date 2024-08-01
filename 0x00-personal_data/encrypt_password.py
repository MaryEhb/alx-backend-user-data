#!/usr/bin/env python3
"""5. Encrypting passwords"""
import bcrypt


def hash_password(password: str) -> bytes:
    """expects one string argument name password and returns a
    salted, hashed password, which is a byte string"""
    en = password.encode()
    hashing = bcrypt.hashpw(en, bcrypt.gensalt())

    return hashing


def is_valid(hashed_password: bytes, password: str) -> bool:
    """expects 2 arguments and returns a boolean"""
    valid = False
    en = password.encode()
    if bcrypt.checkpw(en, hashed_password):
        valid = True
    return valid
