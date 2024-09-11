#!/usr/bin/env python3
"""Authentication module"""
import bcrypt


def _hash_password(password: str) -> bytes:
    """takes in a password string arguments and returns bytes"""
    encoded = password.encode("utf-8")
    salted = bcrypt.gensalt()
    return bcrypt.hashpw(encoded, salted)
