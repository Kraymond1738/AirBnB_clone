#!/usr/bin/python3
import uuid
from datetime import datetime
class BaseModel:
    def __init__(self):
        self.ID = uuid.uuid4()
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def getID():
        return self.ID

    def getCreated_at():
        return self.created_at
    def setCreated_at(created_at):
        self.created_at = created_at

    def getUpdate_at():
        return self.updated_at
    
    def setupdate_at():
        self.updated_at = updated_at
    def __str__(self):
        return str(self.ID) + "  "+ str(self.created_at) +"  "+ str(self.updated_at)
 
    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        return self.__dict__

element = BaseModel()
