#!/usr/bin/python3
"""serialisation and desérialisation with Json"""
from models.base_model import BaseModel
from uuid import uuid4
import json
import os.path
class FileStorage:
    """data storage class"""
    __file_path = ""
    __objects = {}

    def all(self):
        """ dictionary of our attributes __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        new_object = self.__objects.__dict__
        new_obj = obj.__dict__
        new_object["id"] =str(self.__class__.__name__)+ "." + new_obj["id"]
        new_object["created_at"] = new_obj["created_at"]
        new_object["updated_at"] = new_obj["updated_at"]

    def save(self):
        """serializes __objects to the JSON file"""
        with open(self.__file_path, 'w') as f:
            json.dump(self.__objects, f)

    def reload(self):
        """deserializes  JSON file to __objects"""
        if os.path.exists(self.__file_path):
            with open(self.__file_path , 'r') as f:
                return json.load(f)
    
