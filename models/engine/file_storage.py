#!/usr/bin/python3
import json
from models.file_storage import FileStorage
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

    def all(self, cls=None):
        """
        Returns the dictionary with all objects of a specific class.
        """
        if cls:
            if cls in self.classes:
                objects = {k: v for k, v in self.__objects.items()
                           if isinstance(v, self.classes[cls])}
                return objects
            else:
                print("** class doesn't exist **")
                return {}
        else:
            return self.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj id>.
        """
        key = obj.id
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
        """
        Deserializes the JSON file to __objects (only if the JSON file
        (__file_path) exists).
        """
        try:
            with open(self.__file_path, "r", encoding="utf-8") as file:
                data = json.load(file)
                for key, obj_dict in data.items():
                    obj_id = key
                    obj_class = self.classes.get(obj_dict['__class__'])
                    if obj_class:
                        self.__objects[obj_id] = obj_class(**obj_dict)
        except FileNotFoundError:
            pass
