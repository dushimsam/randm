#!/usr/bin/python3
"""
This module defines the `State` class, which serves as a blueprint for creating 
state objects within the application.
"""

from models.base_model import BaseModel


class State(BaseModel):
    """
    Represents a state within the application.

    The `State` class extends `BaseModel` and is used to manage and store information 
    related to a specific state. This class provides a structure for representing 
    geographical or administrative regions.

    Attributes:
        name (str): The name of the state, representing its official designation.
    """
    
    name = ""

    def __init__(self, *args, **kwargs):
        """
        Initializes a new `State` instance.

        This method sets up the state attributes either from provided keyword 
        arguments (kwargs) or by using default values. It inherits initialization 
        behavior from the `BaseModel` class.

        Args:
            *args: Variable length argument list (not used in this implementation).
            **kwargs: Dictionary of keyword arguments to initialize the state attributes.
        """
        super().__init__(*args, **kwargs)
