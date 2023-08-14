#!/usr/bin/env python3

"""
User class.
"""
import hashlib
from models.base_model import BaseModel


class User(BaseModel):
    """Class representing a User."""
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """
        Instantiate a user object
        """
        super().__init__(*args, **kwargs)
        if 'password' in kwargs:
            self.set_password(kwargs['password'])

    def set_password(self, password):
        """
        Set the password after encrypting it with MD5
        """
        secure = hashlib.md5()
        secure.update(password.encode("utf-8"))
        self.password = secure.hexdigest()
