#!/usr/bin/python3
"""
This module defines the `User` class, which serves as a blueprint for creating
user objects within the application.
"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    Represents a user within the application.

    The `User` class extends `BaseModel` and is used to manage and store information
    related to individual users. This class facilitates the management of user-specific
    details such as authentication and personal information.

    Attributes:
        email (str): The email address associated with the user account. Used for 
                     user identification and communication.
        password (str): The password for the user account, typically stored in a
                        hashed format for security.
        first_name (str): The user's first name, used for personal identification.
        last_name (str): The user's last name, used for personal identification and 
                         formal communication.
    """
    
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """
        Initializes a new `User` instance.

        This method sets up the user attributes either from provided keyword arguments 
        (kwargs) or by using default values. It ensures that the user object is correctly
        initialized with all necessary attributes by inheriting from the `BaseModel` class.

        Args:
            *args: Variable length argument list (not used in this implementation).
            **kwargs: Dictionary of keyword arguments to initialize the user attributes.
        """
        super().__init__(*args, **kwargs)
