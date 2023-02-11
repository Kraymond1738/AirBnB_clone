#!/usr/bin/python3
"""the first user created"""

from models.base_model import BaseModel

class user(BaseModel):
    """This is our first user"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
