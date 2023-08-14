#!/usr/bin/env python3
""" Place class """

from models.base_model import BaseModel


class Place(BaseModel):
    """Class representing a Place."""
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
    review_ids = []

    @property
    def amenities(self):
        """
        Getter for amenities list.
        """
        if len(self.amenity_ids) > 0:
            return self.amenity_ids
        else:
            return None

    @amenities.setter
    def amenities(self, amenity_obj):
        """
        Setter for amenity_ids.
        """
        if amenity_obj and amenity_obj.id not in self.amenity_ids:
            self.amenity_ids.append(amenity_obj.id)

    @property
    def reviews(self):
        """
        Getter for reviews list.
        """
        if len(self.review_ids) > 0:
            return self.review_ids
        else:
            return None

    @reviews.setter
    def reviews(self, review_obj):
        """
        Setter for review_ids.
        """
        if review_obj and review_obj.id not in self.review_ids:
            self.review_ids.append(review_obj.id)
