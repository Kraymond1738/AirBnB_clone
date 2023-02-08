#!/usr/bin/python3
"""serialization and deserialization"""

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
        
