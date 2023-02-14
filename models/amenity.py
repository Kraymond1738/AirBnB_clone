#!/usr/bin/python3
"""this is for the amenity class"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
     this is the amenity class containing
     name of the amenities
    """

    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
