#!/usr/bin/env python3
""" TestPlace class """

import unittest
from models.place import Place
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):
    """
    Test suite for the Place class.
    """

    def setUp(self):
        """
        Set up a Place instance for testing.
        """
        self.place = Place(city_id="city123",
                           user_id="user123",
                           name="Sample Place",
                           description="A cozy place to stay.",
                           number_rooms=2,
                           number_bathrooms=1,
                           max_guest=3,
                           price_by_night=1500,
                           latitude=40.7128,
                           longitude=-74.0060)

    def test_attributes(self):
        """
        Test if the necessary attributes are present.
        """
        self.assertTrue(hasattr(self.place, "city_id"))
        self.assertTrue(hasattr(self.place, "user_id"))
        self.assertTrue(hasattr(self.place, "name"))
        self.assertTrue(hasattr(self.place, "description"))
        self.assertTrue(hasattr(self.place, "number_rooms"))
        self.assertTrue(hasattr(self.place, "number_bathrooms"))
        self.assertTrue(hasattr(self.place, "max_guest"))
        self.assertTrue(hasattr(self.place, "price_by_night"))
        self.assertTrue(hasattr(self.place, "latitude"))
        self.assertTrue(hasattr(self.place, "longitude"))
        self.assertTrue(hasattr(self.place, "amenity_ids"))
        self.assertTrue(hasattr(self.place, "review_ids"))

    def test_inheritance(self):
        """
        Test if the Place class inherits from BaseModel.
        """
        self.assertIsInstance(self.place, Place)
        self.assertTrue(issubclass(Place, BaseModel))

    def test_amenities_property(self):
        """
        Test the amenities property to get a list of amenity IDs.
        """
        self.assertIsInstance(self.place.amenities, list)

    def test_amenities_setter(self):
        """
        Test the amenities setter to add amenity IDs.
        """
        amenity_id = "amenity123"
        self.place.amenities = amenity_id
        self.assertIn(amenity_id, self.place.amenity_ids)

    def test_reviews_property(self):
        """
        Test the reviews property to get a list of review IDs.
        """
        self.assertIsInstance(self.place.reviews, list)

    def test_reviews_setter(self):
        """
        Test the reviews setter to add review IDs.
        """
        review_id = "review123"
        self.place.reviews = review_id
        self.assertIn(review_id, self.place.review_ids)


if __name__ == '__main__':
    unittest.main()
