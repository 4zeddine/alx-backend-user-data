#!/usr/bin/env python3
"""Module for session Auth views."""
import os
from distutils.dir_util import remove_tree
from typing import Tuple
from models.user import User
from api.v1.views import app_views
from flask import abort, jsonify, request


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def user_login() -> Tuple[str, int]:
    """Login route
    Returns:
        User object in json
    """
    email = request.form.get('email')
    if email is None or len(email.strip()) == 0:
        return jsonify({"error": "email missing"}), 400
    passwrd = request.form.get('password')
    if passwrd is None or len(passwrd.strip()) == 0:
        return jsonify({"error": "password missing"}), 400
    not_found = {"error": "no user found for this email"}
    pass_error = {"error": "wrong password"}
    try:
        get_users = User.search({'email': email})
    except Exception:
        return jsonify(not_found), 404
    if len(get_users) <= 0:
        return jsonify(not_found), 404
    if get_users[0].is_valid_password(passwrd):
        from api.v1.app import auth
        new_session = auth.create_session(getattr(get_users[0], 'id'))
        res_dict = jsonify(get_users[0].to_json())
        res_dict.set_cookie(os.getenv("SESSION_NAME"), new_session)
        return res_dict
    return jsonify(pass_error), 401

@app_views.route('/auth_session/logout', methods=['DELETE'], strict_slashes=False)
def user_logout() -> Tuple[str, int]:
    """Route for Logout
    Returns:
        empty Json object
    """
    from api.v1.app import auth
    deleted_session = auth.destroy_session(request)
    if not deleted_session:
        abort(404)
    return jsonify({}), 200
