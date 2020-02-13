#!/usr/bin/python3
"""
FileStorage Class

"""
import json
import os


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        FileStorage.__objects["{}.{}".format(obj.__class__.__name__,
                                             obj.id)] = str(obj.__dict__)

    def save(self):
        with open(FileStorage.__file_path, 'w') as file:
            json.dump(FileStorage.__objects, file)

    def reload(self):
        aux = {}
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as file:
                aux = json.load(file)
                for k, v in aux.items():
                    FileStorage.__objects[k] = v
