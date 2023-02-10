#!/usr/bin/python3

"""Basemodel class and the public instance attributes"""
from uuid import uuid4
from datetime import datetime
import model import storage


class BaseModel:
    """
    This contains  all the common attributes
    and other classes inherit from this class
    """

    def __init__(self, *args, **kwargs):
        """intializing the BaseModel class"""

        date_format = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(value, date_format)
                else:
                    self.__dict__[key] = value
        else:
            storage.new(self)

    def __str__(self):
        """define a string representation of the object"""
        name1 = self.__class__.__name__
        return "[{}] ({}) {}".format(name1, self.id, self.__dict__)

    def save(self):
        """updates the updated_at time"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        returns a dictionary containing
        all keys/values of __dict__ of the instance
        """
        res = self.__dict__.copy()
        res["__class__"] = self.__class__.__name__
        res["created_at"] = self.created_at.isoformat()
        res["updated_at"] = self.updated_at.isoformat()
        return res
