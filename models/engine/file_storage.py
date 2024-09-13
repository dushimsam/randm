#!/usr/bin/python3
"""
This module defines the `FileStorage` class, which is responsible for managing
the persistence of objects to and from a JSON file. It provides mechanisms for
storing, retrieving, and reloading objects.
"""

import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """
    Manages the storage and retrieval of objects using a JSON file.

    The `FileStorage` class handles the serialization and deserialization of
    objects, enabling persistence between application runs. It provides methods
    for adding new objects, saving them to a file, and reloading them.

    Attributes:
        __file_path (str): The path to the JSON file where objects are stored.
        __objects (dict): A dictionary holding all objects, with keys formatted
                          as '<class_name>.<object_id>'.
    """
    
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Retrieves all objects currently stored in the dictionary.

        This method returns a dictionary of all objects that have been added to
        the storage. The dictionary keys are formatted as '<class_name>.<object_id>',
        and the values are the corresponding object instances.

        Returns:
            dict: A dictionary of all stored objects.
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Adds a new object to the storage system.

        This method stores the given object in the internal dictionary with a key
        that combines the object's class name and its unique identifier.

        Args:
            obj (object): The object to be added to the storage.
        """
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """
        Persists all objects in the internal dictionary to a JSON file.

        The method serializes each object by calling its `to_dict` method and
        writes the resulting dictionary to the specified JSON file. If the file
        does not exist or is not accessible, the operation is silently ignored.
        """
        obj_dict = {}

        for key, value in self.__objects.items():
            obj_dict[key] = value.to_dict()

        try:
            with open(self.__file_path, 'w') as file:
                json.dump(obj_dict, file, indent=2)
        except FileNotFoundError:
            pass

    def reload(self):
        """
        Reloads objects from the JSON file into the storage system.

        This method reads the JSON file and deserializes the data into objects
        by evaluating the class names and instantiating the corresponding
        objects with their attributes. If the file is not found, the method
        silently does nothing.
        """
        try:
            with open(FileStorage.__file_path, 'r') as file:
                obj_dict = json.load(file)

                for key, value in obj_dict.items():
                    # Reconstruct the object from the dictionary representation
                    class_name = value['__class__']
                    cls = globals().get(class_name, BaseModel)
                    self.__objects[key] = cls(**value)

        except FileNotFoundError:
            pass
