#!/usr/bin/python3
"""the review class description"""
from models.base_models import BaseModel


class Review(BaseModel):
    """
    the review class contains the place_id,
    user_id and a text
    """

    place_id = ""
    user_id = ""
    text = ""

    def __init__(self,*args,**kwargs):
        super().__init__(self,*args,**kwargs)
