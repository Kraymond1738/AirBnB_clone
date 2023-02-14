#!/usr/bin/python3
"""serialization and deserialization"""
import json
import os
import sys
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
class FileStorage:
    """for storage in JSON"""

    __file_path = ""
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        classname = obj.__class__.__name__
        obj_key = f"{classname}.{obj.id}"
        FileStorage.__objects[obj_key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        old_dct = FileStorage.__objects.to_dict()
        new_dct = {key: old_dict[key] for key in old_dct.items()}
        with open(FileStorage__file_path, 'w') as f:
            json.dump(new_dct, f)

    def reload():
        """Deserialize the JSON file __file_path to __objects"""
        try:
            with open(FileStorage.__file_path) as f:
                FileStorage.__objects = json.load(f)
        except FileNotFoundError:
            return
