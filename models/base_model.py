#!/usr/bin/python3
"""
Module for the Base Class
"""
import uuid
from datetime import datetime


class BaseModel:
    def __init__(self, *args, **kwargs):
        """Base Model Instance"""
        if len(kwargs) > 0:
            for k in kwargs.keys():
                v = kwargs[k]
                if k in ["created_at", "updated_at"]:
                    self.__dict__[k] = datetime\
                                    .strptime(v, '%Y-%m-%dT%H:%M:%S.%f')
                elif k == '__class__':
                    del kwargs['__class__']
                else:
                    setattr(self, k, v)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """Return string representation of the object."""
        return "[{}] ({}) {}".format(
            self.__class__.__name__,
            self.id,
            self.__dict__
        )

    def save(self):
        """Update the 'updated_at' timestamp to the current datetime."""
        self.updated_at = datetime.now()

    def to_dict(self):
        """returns a dictionary containing all keys/values"""
        dict_obj = self.__dict__.copy()
        class_name = self.__class__.__name__
        created_at_ = self.created_at.isoformat()
        updated_at_ = self.updated_at.isoformat()
        dict_obj['__class__'] = class_name
        dict_obj['created_at'] = created_at_
        dict_obj['updated_at'] = updated_at_

        return dict_obj
