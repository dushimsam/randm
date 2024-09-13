#!/usr/bin/python3
"""The `amenity` module, containing the Amenity class

This module defines the `Amenity` class, 
which inherits from the `BaseModel` class.
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Represents a specific amenity or feature available at a property.

    Attributes:
        name (str): The name of the amenity or feature provided.
    """

    name = ""
