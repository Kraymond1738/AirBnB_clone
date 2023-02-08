#!/usr/bin/python3
"""Basemodel class and the public instance attributes"""
from uuid import uuid4
from datetime import datetime

class BaseModel:
	"""This contains  all the common attributes and other classes inherit from this class"""
	def __init__(self, *args, **kwargs):
		"""intializing the BaseModel class"""
		self.id = str(uuid4())
		self.created_at = datetime.now()
		self.updated_at = datetime.now()

	def __str__(self):
		"""define a string representation of the object"""
        	return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

	def save(self):
		"""updates the updated_at time"""
		self.updated_at = datetime.now()

	def to_dict(self):
		"""returns a dictionary containing all keys/values of __dict__ of the instance"""
		res = self.__dict__.copy
		res["__class"] = self.__class__.__name__
		res["created_at"] = self.created_at.isoformat()
		res["updated_at"] = self.created_at.isoformat()
		return res
