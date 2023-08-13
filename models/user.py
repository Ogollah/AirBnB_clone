#!/usr/bin/env python3

from models.base_model import BaseModel
"""
User class.
"""


class User(BaseModel):
    """Class representing a User."""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
