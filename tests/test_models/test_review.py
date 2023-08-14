#!/usr/bin/env python3
"""
TestReview Class
"""

import unittest
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    """
    Test suite for the Review class.
    """

    def setUp(self):
        """
        Set up a Review instance for testing.
        """
        self.review = Review(place_id="place123",
                             user_id="user123",
                             text="This is my review.")

    def test_attributes(self):
        """
        Test if the necessary attributes are present.
        """
        self.assertTrue(hasattr(self.review, "place_id"))
        self.assertTrue(hasattr(self.review, "user_id"))
        self.assertTrue(hasattr(self.review, "text"))

    def test_inheritance(self):
        """
        Test if the Review class inherits from BaseModel.
        """
        self.assertIsInstance(self.review, Review)
        self.assertTrue(issubclass(Review, BaseModel))

    def test_text_content(self):
        """
        Test if the text attribute contains the expected content.
        """
        self.assertEqual(self.review.text, "This is a review.")

    def test_init_without_text(self):
        """
        Test the initialization without providing a text.
        """
        review_without_text = Review(place_id="place123", user_id="user123")
        self.assertEqual(review_without_text.text, "")


if __name__ == '__main__':
    unittest.main()
