#!/usr/bin/python3
"""
This module defines the `Review` class, which serves as a blueprint for creating 
review objects within the application.
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """
    Represents a review associated with a specific place or user.

    The `Review` class extends `BaseModel` and includes attributes related to 
    user feedback on a place. This class is used to manage and store reviews 
    within the application.

    Attributes:
        place_id (str): Unique identifier for the place being reviewed.
        user_id (str): Unique identifier for the user who wrote the review.
        text (str): The content of the review provided by the user.
    """
    
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """
        Initializes a new `Review` instance.

        This method sets up the review attributes either from provided keyword 
        arguments (kwargs) or by using default values. Inherited attributes 
        are initialized by the parent class `BaseModel`.

        Args:
            *args: Variable length argument list (not used in this implementation).
            **kwargs: Dictionary of keyword arguments to initialize the review attributes.
        """
        super().__init__(*args, **kwargs)

