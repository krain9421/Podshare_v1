#!/usr/bin/python3
"""This module contains the BaseModel class that defines all common attributes/methods for other classes.
"""
import uuid # Unique User Identification
import models
from datetime import datetime
# from models import storage


class BaseModel:
    """BaseModel class

    Attributes
        id (string): The unique id of the object
        created_at (datetime): The time when an instance is created
        updated_at (datetime): The time to be updated when an object
                                        is changed
    """

    def __init__(self, *args, **kwargs):
        """Function that initializes a BaseModel object"""
        if kwargs: # Condition for initializing a BaseModel object with a dict
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)

            if kwargs.get("created_at", None) and type(self.created_at) is str:
                self.created_at = datetime.fromisoformat(kwargs["created_at"])
            else:
                self.created_at = datetime.today()
            if kwargs.get("updated_at", None) and type(self.updated_at) is str:
                self.updated_at = datetime.fromisoformat(kwargs["updated_at"])
            else:
                self.updated_at = datetime.now()
            if kwargs.get("id", None) is None:
                self.id = str(uuid.uuid4())

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.today()
            self.updated_at = datetime.now()
            # storage.new(self)

    def save(self):
        """Updates the public instance attribute `updated_at` with
                    the current datetime.
        """
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()
        # storage.save()

    def __str__(self):
        """Returns the printable representation of the BaseModel."""
        rep = self.__class__.__name__
        return "[{}] ({}) {}".format(rep, self.id, self.__dict__)

    def to_dict(self):
        """Returns the printable representation of the BaseModel."""
        my_dict = self.__dict__.copy()
        my_dict.update(__class__=self.__class__.__name__)
        my_dict.update(created_at=self.created_at.isoformat())
        my_dict.update(updated_at=self.updated_at.isoformat())
        return my_dict

    def delete(self):
        """delete the current instance from the storage"""
        models.storage.delete(self)
