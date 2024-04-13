#!/usr/bin/python3
import uuid
from datetime import datetime
"""BaseModel"""


class BaseModel:
    def __init__(self, *args, **kwargs):
        """Base Model Instance"""
        if len(kwargs) > 0:
            for k, v in kwargs.items():
                if k in ["created_at", "updated_at"]:
                    self.__dict__[k] = datetime\
                                    .strptime(v, '%Y-%m-%dT%H:%M:%S.%f')
                elif k == 'id':
                    self.id = v
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def save(self):
        """Update the 'updated_at' timestamp to the current datetime."""
        self.updated_at = datetime.now()

    def to_dict(self):
        """returns a dictionary containing all keys/values"""
        class_name = self.__class__.__name__
        created_at_str = self.created_at.isoformat()
        updated_at_str = self.updated_at.isoformat()
        return {'__class__': class_name,
                'id': self.id,
                'created_at': created_at_str,
                'updated_at': updated_at_str,
                **self.__dict__
                }
