#!/usr/bin/python3

"""
This module defines the BaseModel class, which serves as the base class
for other classes.
"""

import uuid
from datetime import datetime


class BaseModel:
    """
    BaseModel class for common attributes and methods.

    Attributes:
        id (str): A unique identifier generated using UUID.
        created_at (datetime): The creation timestamp.
        updated_at (datetime): The last update timestamp.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of the BaseModel class.

        It assigns a unique ID and timestamps. If kwargs is provided,
        it populates the instance attributes.

        Args:
            *args: Unused.
            **kwargs: Dictionary with attribute values.
        """
        from . import storage
        tf = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs:
            if "id" not in kwargs:
                kwargs["id"] = str(uuid.uuid4())
            if "created_at" in kwargs:
                kwargs["created_at"] = datetime.strptime(kwargs["created_at"],
                                                         tf)
            if "updated_at" in kwargs:
                kwargs["updated_at"] = datetime.strptime(kwargs["updated_at"],
                                                         tf)
            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)

    def __str__(self):
        """
        Returns a string representation of the BaseModel.

        Returns:
            str: A formatted string with class name, ID,
            and dictionary representation.
        """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        from . import storage
        """Update the `updated_at` attribute with the current datetime."""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        Converts the BaseModel instance to a dictionary representation.

        Returns:
            dict: A dictionary containing instance attributes
            with proper formatting.
        """
        class_name = self.__class__.__name__
        data = self.__dict__.copy()
        data['__class__'] = class_name
        data['created_at'] = self.created_at.isoformat()
        data['updated_at'] = self.updated_at.isoformat()
        return data
