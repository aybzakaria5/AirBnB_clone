#!/usr/bin/python3
import json
from models.user import User
from models.base_model import BaseModel

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
    }

    def all(sielf, cls=None):
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
        """
        Deserializes the JSON file to __objects (only if the JSON file
        (__file_path) exists).
        """
        try:
            with open(self.__file_path, "r", encoding="utf-8") as file:
                data = json.load(file)
                for key, obj_dict in data.items():
                    class_name, obj_id = key.split(".")
                    obj_class = self.classes.get(class_name)
                    if obj_class:
                        self.__objects[key] = obj_class(**obj_dict)
        except FileNotFoundError:
            pass
