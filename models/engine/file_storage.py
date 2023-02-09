#!/usr/bin/python3
"""serialization and deserialization"""
import json
import os
import sys
sys.path.append(models)
import models.base_model

class FileStorage:
    """for storage in JSON"""
    
    def __init__(self):
        """initializes the class FileStorage"""
        self.__file_path = ""
        self.__objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        classname = obj.__class__.__name__
        obj_key = f"{classname}.{obj.id}"
        self.__objects[obj_key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        old_dct = self.__objects.to_dict()
        new_dct = {key: old_dict[key] for key in old_dct.items()}
        with open(self.__file_path, 'w') as f:
            json.dump(new_dct,f)

    def reload():
        """Deserialize the JSON file __file_path to __objects"""
        try:
            with open(self.__file_path) as f:
                self.__objects = json.load(f)
        except FileNotFoundError:
            return
