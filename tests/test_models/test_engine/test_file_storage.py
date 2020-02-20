#!/usr/bin/python3
"""
File Storage Unittest Module
"""
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.state import State
from models import storage
import os


class TestFileStorage(unittest.TestCase):
    """File Storage Class Tests"""
    __dict = {'BaseModel': BaseModel(),
              'User': User(),
              'Place': Place(),
              'State': State(),
              'City': City(),
              'Amenity': Amenity(),
              'Review': Review()}

    def setUp(self):
        """Sets up method"""
        pass

    def tearDown(self):
        """Tears down methods"""
        FileStorage._FileStorage__objects = {}
        try:
            os.remove(FileStorage._FileStorage__file_path)
        except IOError:
            pass

    def test_FileStorage_empty(self):
        """File Storage type class test"""
        self.assertEqual(FileStorage, type(FileStorage()))
        self.assertEqual(FileStorage, type(storage))
        self.assertEqual(storage.all(), {})

    def test_FileStorage_init_none(self):
        """File Storage none test"""
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_FileStorage_class_instances(self):
        """File Storage none test"""
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def test_FileStorage_all_class_new(self):
        """File Storage none test"""
        for v in TestFileStorage.__dict.values():
            storage.new(v)
        for k, v in TestFileStorage.__dict.items():
            self.assertIn(k + "." + v.id, storage.all().keys())
            self.assertIn(v, storage.all().values())

    def test_FileStorage_all_class_save(self):
        """File Storage save test"""
        for k, v in TestFileStorage.__dict.items():
            k = v
        storage.save()
        for v in TestFileStorage.__dict.values():
            storage.new(v)
        storage.save()

    def test_FileStorage_new_none(self):
        """File Storage new none test"""
        with self.assertRaises(AttributeError):
            storage.new(None)

    def test_FileStorage_reload_none(self):
        """File Storage reload none test"""
        with self.assertRaises(TypeError):
            storage.reload(None)

    def test_FileStorage_reload(self):
        """File Storage reload test"""
        for k, v in TestFileStorage.__dict.items():
            k = v
        storage.save()
        storage.reload()
        objects = storage.all()
        for k in objects.keys():
            obj = objects[k]
            self.assertTrue(issubclass(type(obj), BaseModel))


if __name__ == '__main__':
    unittest.main()
