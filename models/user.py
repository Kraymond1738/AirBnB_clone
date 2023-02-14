#!/usr/bin/python3
"""the first user created"""

from models.base_model import BaseModel


class User(BaseModel):
    """This is our first user"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
