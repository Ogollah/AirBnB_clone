#!/usr/bin/env python3

import models
from models.base_model import BaseModel
"""
State class
"""


class State(BaseModel):
    """Class representing a State."""
    name = ""

    @property
    def cities(self):
        """
        Getter method, returns a list of City objects linked to the State.
        """
        city_list = []
        all_cities = models.storage.all("City").values()

        for city in all_cities:
            if city.state_id == self.id:
                city_list.append(city)

        return city_list
