#!/usr/bin/python3
"""magic file that makes the folder a package"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload
