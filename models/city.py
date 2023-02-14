#!/usr/bin/python3
"""this is the city class"""
from models.base_model import BaseModel


class City(BaseModel):
    """the city class containing the
       name of the city and its id
    """

    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
