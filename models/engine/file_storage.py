#!/usr/bin/python3
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """
    FileStorage class for serializing and deserializing instances to/from
    a JSON file.
    """
    __file_path = "file.json"
    __objects = {}

    classes = {
            'BaseModel': BaseModel,
            'User': User,
            'State': State,
            'City': City,
            'Amenity': Amenity,
            'Place': Place,
            'Review': Review
            }

    def all(self):
        """./
        Returns the dictionary with all objects of a specific class.
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id.
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file.
        """
        serialized_objects = {key: obj.to_dict() for key, obj in
                              self.__objects.items()}
        with open(self.__file_path, "w", encoding="utf-8") as file:
            json.dump(serialized_objects, file)

    def reload(self):
        ''' deserializes the JSON file to __object
        '''
        loaded_dict = {}
        try:
            with open(FileStorage.__file_path, 'r') as f:
                loaded_dict = json.load(f)
        except FileNotFoundError:
            return
        for k, v in loaded_dict.items():
            class_name = k.split('.')[0]
            if class_name in self.classes:
                obj = self.classes[class_name](**v)
                self.new(obj)