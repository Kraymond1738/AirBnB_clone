#!/usr/bin/python3
"""Basemodel class and the public instance attributes"""
from uuid import uuid4
from datetime import datetime

class BaseModel:
	"""This contains  all the common attributes and other classes inherit from this class"""
	def __init__(self, *args, **kwargs):
		"""intializing the BaseModel class"""
