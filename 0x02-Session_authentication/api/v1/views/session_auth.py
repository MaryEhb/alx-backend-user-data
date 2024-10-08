#!/usr/bin/env python3
'''7. New view for Session Authentication'''
from api.v1.views import app_views
from flask import request, jsonify, abort
from models.user import User
from os import environ


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login():
    """a route POST /auth_session/login"""
    email = request.form.get('email')
    if not email:
        return jsonify({"error": "email missing"}), 400

    password = request.form.get('password')

    if not password:
        return jsonify({"error": "password missing"}), 400
    try:
        user = User.search({'email': email})
        user = user[0]
    except Exception:
        return jsonify({"error": "no user found for this email"}), 404

    if not user:
        return jsonify({"error": "no user found for this email"}), 404

    if not user.is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401

    if not user.is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401

    from api.v1.app import auth

    session = auth.create_session(user.id)
    SESSION_NAME = environ.get("SESSION_NAME")

    res = jsonify(user.to_json())
    res.set_cookie(SESSION_NAME, session)
    return res


@app_views.route('/api/v1/auth_session/logout',
                 methods=['DELETE'], strict_slashes=False)
def logout():
    """logout route"""

    from api.v1.app import auth

    if (auth.destroy_session(request)) is False:
        abort(404)
    return jsonify({}), 200
