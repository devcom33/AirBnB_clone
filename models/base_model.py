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
            self.created_at = datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%f')
            self.updated_at = datetime.now()

    def save(self):
        """Update the 'updated_at' timestamp to the current datetime."""
        self.updated_at = datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%f')

    def to_dict(self):
        """returns a dictionary containing all keys/values"""
        class_name = self.__class__.__name__
        created_at_str = self.created_at.strftime('%Y-%m-%dT%H:%M:%S.%f')
        updated_at_str = self.updated_at.strftime('%Y-%m-%dT%H:%M:%S.%f')
        return {'__class__': class_name,
                'id': self.id,
                'created_at': created_at_str,
                'updated_at': updated_at_str,
                **self.__dict__
                }
    def __str__(self):
        """Return string representation of the object."""
        return "[{}] ({}) {}".format(
            self.__class__.__name__,
            self.id,
            self.__dict__
        )

    def __repr__(self):
        """Return object representation."""
        return "<{}>".format(str(self))
