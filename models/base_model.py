#!/usr/bin/python3
import uuid
from datetime import datetime
class BaseModel:
    def __init__(self):
        self.id = uuid.uuid4()
        current_day = datetime.now()
        self.created_at = current_day
        self.updated_at = current_day   
    
    def __str__(self):
        return str(self.id) + "  "+ str(self.created_at) +"  "+ str(self.updated_at)
 
    def save(self):
        current_day = datetime.now()
        self.updated_at = current_day.isoformat()

    def to_dict(self):
        return self.__dict__

element = BaseModel()
