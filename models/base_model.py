#!/usr/bin/python3
"""
Base Model Class

"""
import uuid
import datetime
import json
from datetime import datetime
from models import storage


class BaseModel:
    """ Class Base """

    def __init__(self, **kwargs):
        """ Init Method """
        if kwargs:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    setattr(self, k, datetime.strptime(v,
                                                       '%Y-%m-%dT%H:%M:%S.%f'))
                elif k == "__class__":
                    setattr(self, k, type(self))
                else:
                    setattr(self, k, v)
        else:
            self.id = str(uuid.uuid4())
            self.updated_at = datetime.now()
            self.created_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """Print __str__"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id,
                                     self.__dict__)

    def save(self):
        """Update date method"""
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Return dict method"""
        dict = self.__dict__.copy()
        dict["__class__"] = type(self).__name__
        dict["created_at"] = dict["created_at"].isoformat()
        dict["updated_at"] = dict["updated_at"].isoformat()
        return dict
