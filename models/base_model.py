#!/usr/bin/python3

"""Basemodel class and the public instance attributes"""
from uuid import uuid4
from datetime import datetime
<<<<<<< HEAD

import models

=======
import models
from models import storage
>>>>>>> 7bac7cf2cd0909f613e87585fb8bc1deb0d0b97e
class BaseModel:
    """
    This contains  all the common attributes
    and other classes inherit from this class
    """

    def __init__(self, *args, **kwargs):
        """intializing the BaseModel class"""
<<<<<<< HEAD
=======

>>>>>>> 7bac7cf2cd0909f613e87585fb8bc1deb0d0b97e
        date_format = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

<<<<<<< HEAD
        if (kwargs) or (kwargs != "__class__"):
            for key, value in kwargs.items():
                 if key == "created_at" or key == "updated_at":
                     self.__dict__[key] = datetime.strptime(value, date_format)
                 else:
                     self.__dict__[key] = value
                    
=======
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(value, date_format)
                else:
                    self.__dict__[key] = value
        else:
            storage.new(self)
>>>>>>> 7bac7cf2cd0909f613e87585fb8bc1deb0d0b97e

    def __str__(self):
        """define a string representation of the object"""
        name1 = self.__class__.__name__
        return "[{}] ({}) {}".format(name1, self.id, self.__dict__)

    def save(self):
        """updates the updated_at time"""
        self.updated_at = datetime.now()
<<<<<<< HEAD
        models.storage.save()
=======
        storage.save()
>>>>>>> 7bac7cf2cd0909f613e87585fb8bc1deb0d0b97e

    def to_dict(self):
        """
        returns a dictionary containing
        all keys/values of __dict__ of the instance
        """
        res = self.__dict__.copy()
<<<<<<< HEAD
        res["__class"] = self.__class__.__name__
        res["created_at"] = self.created_at.isoformat()
        res["updated_at"] = self.created_at.isoformat()
=======
        res["__class__"] = self.__class__.__name__
        res["created_at"] = self.created_at.isoformat()
        res["updated_at"] = self.updated_at.isoformat()
>>>>>>> 7bac7cf2cd0909f613e87585fb8bc1deb0d0b97e
        return res
