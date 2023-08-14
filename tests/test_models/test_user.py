#!/usr/bin/env python3
"""
TestUser class
"""

import unittest
from models.user import User
from models.base_model import BaseModel
import hashlib


class TestUser(unittest.TestCase):
    """
    Test suite for the User class.
    """

    def setUp(self):
        """
        Set up a User instance for testing.
        """
        self.user = User(email="peter@example.com",
                         password="hashpass",
                         first_name="Peter",
                         last_name="Ochieng")

    def test_attributes(self):
        """
        Test if the necessary attributes are present.
        """
        self.assertTrue(hasattr(self.user, "email"))
        self.assertTrue(hasattr(self.user, "password"))
        self.assertTrue(hasattr(self.user, "first_name"))
        self.assertTrue(hasattr(self.user, "last_name"))

    def test_inheritance(self):
        """
        Test if the User class inherits from BaseModel.
        """
        self.assertIsInstance(self.user, User)
        self.assertTrue(issubclass(User, BaseModel))

    def test_password_encryption(self):
        """
        Test if the password is properly encrypted during initialization.
        """
        password_hash = hashlib.md5("password".encode("utf-8")).hexdigest()
        self.assertEqual(self.user.password, password_hash)

    def test_password_setter(self):
        """
        Test the functionality of the password setter.
        """
        self.user.set_password("newpassword")
        new_password_hash = hashlib.md5(
            "newpassword".encode("utf-8")).hexdigest()
        self.assertEqual(self.user.password, new_password_hash)

    def test_init_with_password(self):
        """
        Test the initialization when a password is provided.
        """
        user_with_pwd = User(email="testpass@example.com", password="hash123")
        password_hash = hashlib.md5("hash123".encode("utf-8")).hexdigest()
        self.assertEqual(user_with_pwd.password, password_hash)

    def test_init_without_password(self):
        """
        Test the initialization when a password is not provided.
        """
        user_without_pwd = User(email="testpass@example.com")
        self.assertEqual(user_without_pwd.password, "")


if __name__ == '__main__':
    unittest.main()
