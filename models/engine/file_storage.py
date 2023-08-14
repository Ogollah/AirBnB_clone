#!/usr/bin/python3
"""
FileStorage class.
"""

import json
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """
    A class for managing serialization and
    deserialization of objects using JSON files.

    Attributes:
        __file_path (str): Path to the JSON file where data is stored.
        __objects (dict): Dictionary to store
        objects by their class name and ID.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary containing all stored objects.

        Returns:
            dict: A dictionary of objects organized by class name and ID.
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Adds a new object to the storage dictionary.

        Args:
            obj (BaseModel): The object to be added to the storage.
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """
        Serializes and saves objects to the JSON file.
        """
        serialized_objs = {key: obj.to_dict() for key,
                           obj in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(serialized_objs, f)

    def reload(self):
        """
        Deserializes and loads objects from
        the JSON file (if it exists).
        """
        try:
            with open(FileStorage.__file_path, 'r') as f:
                data = json.load(f)
                for key, obj_data in data.items():
                    class_name = obj_data['__class__']
                    if class_name == 'User':
                        obj = User.create_from_dict(obj_data)
                    elif class_name == 'State':
                        obj = State.create_from_dict(obj_data)
                    elif class_name == 'City':
                        obj = City.create_from_dict(obj_data)
                    elif class_name == 'Amenity':
                        obj = Amenity.create_from_dict(obj_data)
                    elif class_name == 'Place':
                        obj = Place.create_from_dict(obj_data)
                    elif class_name == 'Review':
                        obj = Review.create_from_dict(obj_data)
                    else:
                        obj = globals()[class_name].create_from_dict(obj_data)
                    FileStorage.__objects[key] = obj
        except FileNotFoundError:
            pass
