#!/usr/bin/python3
"""
This module contains the definition for the `City` class.

The `City` class extends from `BaseModel`, inheriting common attributes and methods.
It represents a city entity within the application.
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    Represents a city within the application.

    This class inherits from `BaseModel` and adds specific attributes related to
    cities.

    Attributes:
        name (str): The name of the city.
        state_id (str): The unique identifier of the state to which the city belongs.
    """

    name = ""
    state_id = ""

    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of the `City` class.

        Inherited attributes are initialized by the parent class `BaseModel`.
        Additional city-specific attributes are set from keyword arguments (kwargs)
        if provided.

        Args:
            *args: Variable length argument list (not used in this implementation).
            **kwargs: Dictionary of keyword arguments to initialize attributes.
        """
        super().__init__(*args, **kwargs)

    def __str__(self):
        """
        Provides a human-readable string representation of the `City` instance.

        Returns:
            str: A formatted string showing the class name, ID, and attributes
                 of the city instance.
        """
        return f"[{self.__class__.__name__}] ({self.id}) Name: {self.name}, State ID: {self.state_id}"
