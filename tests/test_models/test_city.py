#!/usr/bin/python3
"""
City Unittest Module
"""
import unittest
from models.base_model import BaseModel
from models.city import City
from models.engine.file_storage import FileStorage
import os
import json
import datetime


class TestCity(unittest.TestCase):
    """City Class Tests"""

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

    def test_subclass_City(self):
        """Test City instance"""
        self.assertTrue(issubclass(City, BaseModel))

    def test_City_basic_instance(self):
        """Test City instance"""
        A = City()
        A.name = "New York"
        self.assertIsInstance(A, BaseModel)
        self.assertEqual(City, type(A))
        self.assertTrue(hasattr(A, "state_id"))
        self.assertTrue(hasattr(A, "created_at"))
        self.assertTrue(hasattr(A, "updated_at"))
        self.assertTrue(hasattr(A, "name"))

    def test_City_basic_instance_none(self):
        """Test City instance None"""
        with self.assertRaises(TypeError):
            City(None)

    def test_City_attr_types(self):
        """Test City instance attributes"""
        U = City()
        U.name = "New York"
        self.assertEqual(type(U.id), str)
        self.assertTrue(type(U.created_at) is datetime.datetime)
        self.assertTrue(type(U.updated_at) is datetime.datetime)
        self.assertEqual(type(U.name), str)

    def test_City_diff_id(self):
        """Test City instance different id"""
        U1 = City()
        U2 = City()
        U3 = City()
        self.assertNotEqual(U1.id, U2.id)
        self.assertNotEqual(U1.id, U3.id)
        self.assertNotEqual(U2.id, U3.id)

    def test_City_str(self):
        """Test City print"""
        U = City()
        s = "[City] ({}) {}".format(U.id, U.__dict__)
        self.assertEqual(s, str(U))

    def test_City_none_kwargs(self):
        """Test City none kwargs"""
        with self.assertRaises(TypeError):
            City(id=None, created_at=None, updated_at=None)

    def test_City_kwargs(self):
        """Test City kwargs"""
        U1 = City()
        U1.name = "New York"
        dict = U1.to_dict()
        U2 = City(**dict)
        self.assertEqual(U1.id, U1.id)
        self.assertEqual(U1.created_at, U2.created_at)
        self.assertEqual(U1.updated_at, U2.updated_at)
        self.assertEqual(U1.name, U2.name)
        self.assertNotEqual(U1, U2)

    def test_City_save_none(self):
        """Tests save no instances"""
        with self.assertRaises(TypeError):
            City.save()

    def test_City_save(self):
        """Tests save"""
        U = City()
        U.name = "New York"
        U.save()
        k = "{}.{}".format(type(U).__name__, U.id)
        dict = {k: U.to_dict()}
        self.assertTrue(os.path.isfile(FileStorage._FileStorage__file_path))
        with open(FileStorage._FileStorage__file_path,
                  "r", encoding="utf-8") as file:
            self.assertEqual(json.load(file), dict)


if __name__ == '__main__':
    unittest.main()
