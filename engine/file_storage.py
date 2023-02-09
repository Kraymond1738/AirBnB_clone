#!/usr/bin/python3
"""serialisation and desérialisation with Json"""
from ../base_model.py import BaseModel
class FileStorage:
    """data storage class"""
    def __init__(self):
        self.__file_path = ""
        self.__objects = new BaseModel()
