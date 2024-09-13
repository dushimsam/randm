#!/usr/bin/python3
"""
This module introduces the BaseModel class,
which serves as a blueprint for all model classes.
"""

import uuid
import models
from datetime import datetime


class BaseModel:
    """
    The core model class that provides fundamental attributes and methods
    for derived classes, including unique identifiers and timestamps.
    """

    def __init__(self, *args, **kwargs):
        """
        Constructs a new BaseModel instance.

        Initializes attributes from keyword arguments (kwargs) if provided,
        otherwise sets default attributes.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key in ('created_at', 'updated_at'):
                    value = datetime.fromisoformat(value)
                if key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def save(self):
        """
        Saves the current state of the instance to storage.

        Updates the `updated_at` timestamp and calls the save method of
        the storage engine to persist changes.
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Converts the instance into a dictionary.

        Includes all instance attributes and formats datetime fields to
        ISO 8601 string format.

        Returns:
            dict: A dictionary representation of the instance.
        """
        instance_dict = dict(self.__dict__)
        instance_dict["__class__"] = self.__class__.__name__
        for attr, value in self.__dict__.items():
            if attr in ('created_at', 'updated_at'):
                instance_dict[attr] = value.isoformat()
            else:
                instance_dict[attr] = value
        return instance_dict

    def __str__(self):
        """
        Provides a string representation of the BaseModel instance.

        Returns:
            str: A formatted string showing the class name, ID, and attributes.
        """
        class_name = self.__class__.__name__
        return f"[{class_name}] ({self.id}) {self.__dict__}"
