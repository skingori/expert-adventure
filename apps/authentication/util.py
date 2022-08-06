# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
from werkzeug.security import generate_password_hash, check_password_hash

# Inspiration -> https://www.vitoshacademy.com/hashing-passwords-in-python/


def hash_pass(password):
    """Hash a password for storing."""
    return generate_password_hash(password)


def verify_pass(provided_password, stored_password):
    """Verify a stored password against one provided by user"""
    return check_password_hash(stored_password, provided_password)
