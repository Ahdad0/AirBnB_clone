#!/usr/bin/python3
"""This module defines the BaseModel class."""
from datetime import datetime
import uuid


class BaseModel:
    """This represents the class."""

    time_format = "%Y-%m-%dT%H:%M:%S.%f"

    def __init__(self, *args, **kwargs):
        """
        Creates an instance of the BaseModel

        Attributes:
            id (str): Unique identifer for each instance.
            created_at (datetime): Date and time of creation of the instance.
            updated_at (datetime): Current datetime when the object is changed.
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        for key, value in kwargs:
            if key is "updated_at" or key is "created_at":
                self.dict[key] = strptime(value, time_format)

    def __str__(self):
        """Returns a string representation of the class."""
        cls_name = self.__class__.__name__
        return "[{}] ({}) {}".format(cls_name, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with the current datetime."""
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary representation of the instance.

        __class__ returns the class name of the instance.
        self.__dict__ returns instance attributes only.
        Converts created_at and updated_at to ISO format.
        """
        new_dict = self.__dict__.copy()
        new_dict["updated_at"] = self.updated_at.isoformat()
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["__class__"] = self.__class__.__name__
