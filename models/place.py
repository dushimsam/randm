#!/usr/bin/python3
"""
This module defines the `Place` class, which serves as a blueprint for creating 
place/house objects within the application.
"""

from models.base_model import BaseModel


class Place(BaseModel):
    """
    Represents a place or house within the application.

    The `Place` class extends `BaseModel` and adds attributes specific to 
    a place or house. This class is used to model various properties of 
    accommodation in the system.
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def __init__(self, *args, **kwargs):
        """
        Initializes a new `Place` instance.

        This method sets up the place/house attributes either from provided
        keyword arguments (kwargs) or by using default values. Inherited
        attributes are initialized by the parent class `BaseModel`.

        Args:
            *args: Variable length argument list (not used in this implementation).
            **kwargs: Dictionary of keyword arguments to initialize the place attributes.
        """
        super().__init__(*args, **kwargs)
