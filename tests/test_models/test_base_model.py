import unittest
from models.base_model import BaseModel
from datetime import datetime
import json
import os

class TestBaseModel(unittest.TestCase):

    def setUp(self):
        """
        Create a BaseModel instance for testing
        """
        self.model = BaseModel()

    def tearDown(self):
        """
        Clean up: Remove the JSON file after each test
        """
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_id_creation(self):
        """
        Test if the instance's id is created
        """
        self.assertIsNotNone(self.model.id)
        self.assertIsInstance(self.model.id, str)

    def test_created_at(self):
        """
        Test if created_at attribute is set as expected
        """
        self.assertIsNotNone(self.model.created_at)
        self.assertIsInstance(self.model.created_at, datetime)

    def test_updated_at(self):
        """
        Test if updated_at attribute is set as expected
        """
        self.assertIsNotNone(self.model.updated_at)
        self.assertIsInstance(self.model.updated_at, datetime)

    def test_save_method(self):
        """
        Test if the save method updates the updated_at attribute
        """
        old_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(old_updated_at, self.model.updated_at)

    def test_to_dict_method(self):
        """
        Test if the to_dict method returns the correct dictionary representation
        """
        obj_dict = self.model.to_dict()
        self.assertIsInstance(obj_dict, dict)
        self.assertIn("__class__", obj_dict)
        self.assertEqual(obj_dict["__class__"], "BaseModel")
        self.assertIn("id", obj_dict)
        self.assertIn("created_at", obj_dict)
        self.assertIn("updated_at", obj_dict)
        self.assertEqual(obj_dict["id"], self.model.id)
        self.assertEqual(obj_dict["created_at"], self.model.created_at.isoformat())
        self.assertEqual(obj_dict["updated_at"], self.model.updated_at.isoformat())

    def test_json_serialization(self):
        """
        Test if the to_dict output can be serialized to JSON
        """
        obj_dict = self.model.to_dict()
        json_str = json.dumps(obj_dict)
        self.assertIsInstance(json_str, str)

    def test_json_deserialization(self):
        """
        Test if a JSON representation can be deserialized back to a dictionary
        """
        obj_dict = self.model.to_dict()
        json_str = json.dumps(obj_dict)
        new_obj_dict = json.loads(json_str)
        self.assertIsInstance(new_obj_dict, dict)
        self.assertIn("__class__", new_obj_dict)
        self.assertEqual(new_obj_dict["__class__"], "BaseModel")
        self.assertIn("id", new_obj_dict)
        self.assertIn("created_at", new_obj_dict)
        self.assertIn("updated_at", new_obj_dict)

if __name__ == '__main__':
    unittest.main()
