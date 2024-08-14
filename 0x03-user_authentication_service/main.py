#!/usr/bin/env python3
"""
Main file
"""


def register_user(EMAIL, PASSWD):
    """register_user(EMAIL, PASSWD)"""
    pass


def log_in_wrong_password(EMAIL, NEW_PASSWD):
    """log_in_wrong_password(EMAIL, NEW_PASSWD)"""
    pass


def profile_unlogged():
    """profile_unlogged()"""
    pass


def log_in(EMAIL, PASSWD):
    """session_id = log_in(EMAIL, PASSWD)"""
    pass


def profile_logged(session_id):
    """profile_logged(session_id)"""
    pass


def log_out(session_id):
    """log_out(session_id)"""
    pass


def reset_password_token(EMAIL):
    """reset_password_token(EMAIL)"""
    pass


def update_password(EMAIL, reset_token, NEW_PASSWD):
    """update_password(EMAIL, reset_token, NEW_PASSWD)"""
    pass


def log_in(EMAIL, NEW_PASSWD):
    """log_in(EMAIL, NEW_PASSWD)"""
    pass


EMAIL = "guillaume@holberton.io"
PASSWD = "b4l0u"
NEW_PASSWD = "t4rt1fl3tt3"


if __name__ == "__main__":

    register_user(EMAIL, PASSWD)
    log_in_wrong_password(EMAIL, NEW_PASSWD)
    profile_unlogged()
    session_id = log_in(EMAIL, PASSWD)
    profile_logged(session_id)
    log_out(session_id)
    reset_token = reset_password_token(EMAIL)
    update_password(EMAIL, reset_token, NEW_PASSWD)
    log_in(EMAIL, NEW_PASSWD)
