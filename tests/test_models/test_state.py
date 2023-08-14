#!/usr/bin/env python3
"""
TestState class
"""

import unittest
from models.state import State
from models.city import City
from models.base_model import BaseModel
import models


class TestState(unittest.TestCase):
    """
    Test suite for the State class.
    """

    def setUp(self):
        """
        Set up a State instance for testing.
        """
        self.state = State(name="Kenya")
        self.city1 = City(name="Mombasa", state_id=self.state.id)
        self.city2 = City(name="Kisumu", state_id=self.state.id)

    def test_attributes(self):
        """
        Test if the necessary attributes are present.
        """
        self.assertTrue(hasattr(self.state, "name"))

    def test_inheritance(self):
        """
        Test if the State class inherits from BaseModel.
        """
        self.assertIsInstance(self.state, State)
        self.assertTrue(issubclass(State, BaseModel))

    def test_cities_property(self):
        """
        Test the cities property to get a list of linked City objects.
        """
        self.assertIsInstance(self.state.cities, list)

    def test_cities_linked_to_state(self):
        """
        Test if the cities linked to the state are correctly retrieved.
        """
        cities_linked = [self.city1, self.city2]
        self.assertEqual(self.state.cities, cities_linked)

    def test_cities_linked_to_wrong_state(self):
        """
        Test if cities linked to other states are not retrieved.
        """
        state2 = State(name="Kenya")
        city3 = City(name="Nairobi", state_id=state2.id)
        models.storage.new(state2)
        models.storage.new(city3)
        self.assertNotIn(city3, self.state.cities)


if __name__ == '__main__':
    unittest.main()
