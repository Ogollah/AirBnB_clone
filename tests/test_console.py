#!/usr/bin/env python3
"""TestHBNBCommand class"""

import unittest
import io
import sys
import unittest.mock
from unittest import TestCase
from models.base_model import BaseModel
from models import storage
from console import HBNBCommand


class TestHBNBCommand(TestCase):
    """
    Test suite for the HBNBCommand class.
    """

    def setUp(self):
        """
        Set up the HBNBCommand instance for testing.
        """
        self.hbnb_cmd = HBNBCommand()
        self.base_model = BaseModel()
        storage.new(self.base_model)

    def tearDown(self):
        """
        Clean up after testing.
        """
        storage.delete(self.base_model)
        if hasattr(self.hbnb_cmd, "data_stream"):
            self.hbnb_cmd.data_stream.close()

    def test_create_command(self):
        """
        Test the create command.
        """
        with unittest.mock.patch("sys.stdout",
                                 new_callable=io.StringIO) as mock_stdout:
            self.hbnb_cmd.onecmd("create BaseModel")
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, self.base_model.id)

    def test_show_command(self):
        """
        Test the show command.
        """
        with unittest.mock.patch("sys.stdout",
                                 new_callable=io.StringIO) as mock_stdout:
            self.hbnb_cmd.onecmd(
                "show BaseModel {}".format(self.base_model.id))
            output = mock_stdout.getvalue().strip()
            self.assertIn(self.base_model.id, output)

    def test_destroy_command(self):
        """
        Test the destroy command.
        """
        obj_id = self.base_model.id
        key = "{}.{}".format(self.base_model.__class__.__name__, obj_id)
        with unittest.mock.patch("sys.stdout",
                                 new_callable=io.StringIO) as mock_stdout:
            self.hbnb_cmd.onecmd("destroy BaseModel {}".format(obj_id))
            output = mock_stdout.getvalue().strip()
            self.assertFalse(key in storage.all())

    def test_all_command(self):
        """
        Test the all command.
        """
        with unittest.mock.patch("sys.stdout",
                                 new_callable=io.StringIO) as mock_stdout:
            self.hbnb_cmd.onecmd("all")
            output = mock_stdout.getvalue().strip()
            self.assertIn(self.base_model.id, output)

    def test_update_command(self):
        """
        Test the update command.
        """
        attr_name = "name"
        attr_value = "New Name"
        with unittest.mock.patch("sys.stdout",
                                 new_callable=io.StringIO) as mock_stdout:
            self.hbnb_cmd.onecmd("update BaseModel {} {} \"{}\"".format(
                self.base_model.id, attr_name, attr_value))
            output = mock_stdout.getvalue().strip()
            self.assertIn(attr_value, output)

    def test_wrong_class_name(self):
        """
        Test wrong class name scenarios.
        """
        with unittest.mock.patch("sys.stdout",
                                 new_callable=io.StringIO) as mock_stdout:
            self.hbnb_cmd.onecmd("create WrongModel")
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "** class doesn't exist **")

    def test_wrong_instance_id(self):
        """
        Test wrong instance id scenarios.
        """
        with unittest.mock.patch("sys.stdout",
                                 new_callable=io.StringIO) as mock_stdout:
            self.hbnb_cmd.onecmd("show BaseModel wrong_id")
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "** no instance found **")

    def test_empty_command(self):
        """
        Test empty command scenario.
        """
        with unittest.mock.patch("sys.stdout",
                                 new_callable=io.StringIO) as mock_stdout:
            self.hbnb_cmd.onecmd("")
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "")


if __name__ == '__main__':
    unittest.main()
