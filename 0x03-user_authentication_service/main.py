#!/usr/bin/env python3
"""Module for main, test for app"""
import requests


EMAIL = "guillaume@holberton.io"
PASSWD = "b4l0u"
NEW_PASSWD = "t4rt1fl3tt3"
BASE_URL = "http://0.0.0.0:5000"


def register_user(email: str, password: str) -> None:
    """tests the registration of a user"""
    url = "{}/users".format(BASE_URL)
    body = {
        'email': email,
        'password': password,
    }
    data = requests.post(url, data=body)
    assert data.status_code == 200
    assert data.json() == {"email": email, "message": "user created"}
    data = requests.post(url, data=body)
    assert data.status_code == 400
    assert data.json() == {"message": "email already registered"}


def log_in_wrong_password(email: str, password: str) -> None:
    """tests the wrong password login"""
    url = "{}/sessions".format(BASE_URL)
    body = {
        'email': email,
        'password': password,
    }
    data = requests.post(url, data=body)
    assert data.status_code == 401


def log_in(email: str, password: str) -> str:
    """tests the logging in"""
    url = "{}/sessions".format(BASE_URL)
    body = {
        'email': email,
        'password': password,
    }
    data = requests.post(url, data=body)
    assert data.status_code == 200
    assert data.json() == {"email": email, "message": "logged in"}
    return data.cookies.get('session_id')


def profile_unlogged() -> None:
    """tests the logged out getting profile info"""
    url = "{}/profile".format(BASE_URL)
    data = requests.get(url)
    assert data.status_code == 403


def profile_logged(session_id: str) -> None:
    """tests the logged in getting profile info"""
    url = "{}/profile".format(BASE_URL)
    req_cookies = {
        'session_id': session_id,
    }
    data = requests.get(url, cookies=req_cookies)
    assert data.status_code == 200
    assert "email" in data.json()


def log_out(session_id: str) -> None:
    """tests the session logout"""
    url = "{}/sessions".format(BASE_URL)
    req_cookies = {
        'session_id': session_id,
    }
    data = requests.delete(url, cookies=req_cookies)
    assert data.status_code == 200
    assert data.json() == {"message": "Bienvenue"}


def reset_password_token(email: str) -> str:
    """tests the password reset"""
    url = "{}/reset_password".format(BASE_URL)
    body = {'email': email}
    data = requests.post(url, data=body)
    assert data.status_code == 200
    assert "email" in data.json()
    assert data.json()["email"] == email
    assert "reset_token" in data.json()
    return data.json().get('reset_token')


def update_password(email: str, reset_token: str, new_password: str) -> None:
    """tests user password update"""
    url = "{}/reset_password".format(BASE_URL)
    body = {
        'email': email,
        'reset_token': reset_token,
        'new_password': new_password,
    }
    data = requests.put(url, data=body)
    assert data.status_code == 200
    assert data.json() == {"email": email, "message": "Password updated"}


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
