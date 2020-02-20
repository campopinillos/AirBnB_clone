#!/usr/bin/python3
"""
Place Unittest Module
"""
import unittest
from models.base_model import BaseModel
from models.place import Place
from models.engine.file_storage import FileStorage
import os
import pep8
import json
import datetime


class TestPlace(unittest.TestCase):
    """Place Class Tests"""

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

    def test_pep8_conformance(self):
        """Tests Pep8"""
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['models/place.py'])
        self.assertEqual(result.total_errors, 0, "Fix pep8")

    def test_subclass_Place(self):
        """Test Place instance"""
        self.assertTrue(issubclass(Place, BaseModel))

    def test_Place_basic_instance(self):
        """Test Place instance"""
        A = Place()
        self.assertIsInstance(A, Place)
        self.assertEqual(Place, type(A))
        self.assertTrue(hasattr(A, "id"))
        self.assertTrue(hasattr(A, "created_at"))
        self.assertTrue(hasattr(A, "updated_at"))
        self.assertTrue(hasattr(A, "city_id"))
        self.assertTrue(hasattr(A, "user_id"))
        self.assertTrue(hasattr(A, "name"))
        self.assertTrue(hasattr(A, "description"))
        self.assertTrue(hasattr(A, "number_rooms"))
        self.assertTrue(hasattr(A, "number_bathrooms"))
        self.assertTrue(hasattr(A, "max_guest"))
        self.assertTrue(hasattr(A, "price_by_night"))
        self.assertTrue(hasattr(A, "latitude"))
        self.assertTrue(hasattr(A, "longitude"))
        self.assertTrue(hasattr(A, "amenity_ids"))

    def test_Place_basic_instance_none(self):
        """Test Place instance None"""
        with self.assertRaises(TypeError):
            BaseModel(None)

    def test_Place_attr_types(self):
        """Test Place instance attributes"""
        U = Place()
        U.name = "CampSpace"
        self.assertEqual(type(U.id), str)
        self.assertTrue(type(U.created_at) is datetime.datetime)
        self.assertTrue(type(U.updated_at) is datetime.datetime)
        self.assertEqual(type(U.city_id), str)
        self.assertEqual(type(U.name), str)
        self.assertEqual(type(U.name), str)
        self.assertEqual(type(U.name), str)
        self.assertEqual(type(U.name), str)
        self.assertEqual(type(U.name), str)
        self.assertEqual(type(U.name), str)
        self.assertEqual(type(U.name), str)

    def test_Place_diff_id(self):
        """Test Place instance different id"""
        U1 = Place()
        U2 = Place()
        U3 = Place()
        self.assertNotEqual(U1.id, U2.id)
        self.assertNotEqual(U1.id, U3.id)
        self.assertNotEqual(U2.id, U3.id)

    def test_Place_str(self):
        """Test Place print"""
        U = Place()
        s = "[Place] ({}) {}".format(U.id, U.__dict__)
        self.assertEqual(s, str(U))

    def test_Place_none_kwargs(self):
        """Test Place none kwargs"""
        with self.assertRaises(TypeError):
            Place(id=None, created_at=None, updated_at=None)

    def test_Place_kwargs(self):
        """Test Place kwargs"""
        U1 = Place()
        U1.name = "Holberton"
        dict = U1.to_dict()
        U2 = Place(**dict)
        self.assertEqual(U1.id, U1.id)
        self.assertEqual(U1.created_at, U2.created_at)
        self.assertEqual(U1.updated_at, U2.updated_at)
        self.assertEqual(U1.name, U2.name)
        self.assertNotEqual(U1, U2)

    def test_Place_save_none(self):
        """Tests save no instances"""
        with self.assertRaises(TypeError):
            Place.save()

    def test_Place_save(self):
        """Tests save"""
        U = Place()
        U.name = "Space"
        U.email = "123@mail.com"
        U.save()
        k = "{}.{}".format(type(U).__name__, U.id)
        dict = {k: U.to_dict()}
        self.assertTrue(os.path.isfile(FileStorage._FileStorage__file_path))
        with open(FileStorage._FileStorage__file_path,
                  "r", encoding="utf-8") as file:
            self.assertEqual(json.load(file), dict)

    def test_amenity_save_more_args(self):
        """Tests save with more arguments"""
        with self.assertRaises(TypeError):
            Place.save(self, 1, "Hello")


if __name__ == '__main__':
    unittest.main()
