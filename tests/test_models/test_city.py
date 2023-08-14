#!/usr/bin/env python3
""" TestCity class """

import unittest
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """
    Test suite for the City class.
    """

    def setUp(self):
        """
        Set up a City instance for testing.
        """
        self.city = City(state_id="state123", name="Nairobi City")

    def test_attributes(self):
        """
        Test if the necessary attributes are present.
        """
        self.assertTrue(hasattr(self.city, "state_id"))
        self.assertTrue(hasattr(self.city, "name"))
        self.assertTrue(hasattr(self.city, "places"))

    def test_inheritance(self):
        """
        Test if the City class inherits from BaseModel.
        """
        self.assertIsInstance(self.city, City)
        self.assertTrue(issubclass(City, BaseModel))

    def test_places_attribute(self):
        """
        Test the places attribute is a list.
        """
        self.assertIsInstance(self.city.places, list)

    def test_places_content(self):
        """
        Test the places attribute is empty initially.
        """
        self.assertEqual(len(self.city.places), 0)


if __name__ == '__main__':
    unittest.main()
