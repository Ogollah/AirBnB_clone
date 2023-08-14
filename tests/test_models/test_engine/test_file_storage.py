#!/usr/bin/env python3
"""
TestFileStorage class
"""

import unittest
import os
import json
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):

    def setUp(self):
        """
        Create a FileStorage instance and a BaseModel instance for testing
        """
        self.storage = FileStorage()
        self.model = BaseModel()
        self.storage.new(self.model)

    def tearDown(self):
        """
        Clean up: Remove the JSON file after each test
        """
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_new_method(self):
        """
        Test if the new method adds the instance to the internal dictionary
        """
        key = "{}.{}".format(self.model.__class__.__name__, self.model.id)
        self.assertIn(key, self.storage.all())

    def test_save_method(self):
        """
        Test if the save method serializes instances to the JSON file
        """
        key = "{}.{}".format(self.model.__class__.__name__, self.model.id)
        self.storage.save()
        with open("file.json", "r") as f:
            data = json.load(f)
            self.assertIn(key, data)

    def test_reload_method(self):
        """
        Test if the reload method correctly deserializes
        instances from the JSON file
        """
        self.storage.save()
        self.storage.reload()
        key = "{}.{}".format(self.model.__class__.__name__, self.model.id)
        self.assertIn(key, self.storage.all())

    def test_reload_file_not_exists(self):
        """
        Test if the reload method works when the JSON file does not exist
        """
        self.storage.reload()
        self.assertEqual(len(self.storage.all()), 0)


if __name__ == '__main__':
    unittest.main()
