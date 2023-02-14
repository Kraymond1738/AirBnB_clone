#!/usr/bin/python3
"""the state class"""

from models.base_model import BaseModel


class State(BaseModel):
    """describes the state and its attributes"""

    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
