#!/usr/bin/python3
"""
FileStorage Module

"""
import json
import os


class FileStorage:
    """Class FileStorage engine"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Method to return all the objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Method to save a new object"""
        FileStorage.__objects["{}.{}".format(obj.__class__.__name__,
                                             obj.id)] = obj

    def save(self):
        """Method to serialize all the objects in a JSON file"""
        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            dict = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
            json.dump(dict, file)

    def reload(self):
        """Method to deserialize all the objects from a JSON file"""
        if os.path.exists(FileStorage.__file_path):
            from models.base_model import BaseModel
            from models.user import User
            from models.city import City
            from models.amenity import Amenity
            from models.place import Place
            from models.review import Review
            from models.state import State
            with open(FileStorage.__file_path, "r") as file:
                obj = json.load(file)
                for v in obj.values():
                    print(eval(v["__class__"]))
                    self.new(eval(v["__class__"])(**v))
