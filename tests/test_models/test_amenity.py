#!/usr/bin/python3
"""
Amenity Unittest Module
"""
import unittest
from models.base_model import BaseModel
from models.amenity import Amenity
from models.engine.file_storage import FileStorage
import os
import pep8
import json
import datetime


class TestAmenity(unittest.TestCase):
    """Amenity Class Tests"""

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
        """ Tests pep8 """
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['models/amenity.py'])
        self.assertEqual(result.total_errors, 0, "fix pep8")

    def test_subclass_Amenity(self):
        """Test Amenity instance"""
        self.assertTrue(issubclass(Amenity, BaseModel))

    def test_Amenity_basic_instance(self):
        """Test Amenity instance"""
        A = Amenity()
        A.name = "Space"
        self.assertIsInstance(A, Amenity)
        self.assertEqual(Amenity, type(A))
        self.assertTrue(hasattr(A, "id"))
        self.assertTrue(hasattr(A, "created_at"))
        self.assertTrue(hasattr(A, "updated_at"))
        self.assertTrue(hasattr(A, "name"))

    def test_Amenity_basic_instance_none(self):
        """Test Amenity instance None"""
        with self.assertRaises(TypeError):
            BaseModel(None)

    def test_Amenity_attr_types(self):
        """Test Amenity instance attributes"""
        U = Amenity()
        U.name = "Space"
        self.assertEqual(type(U.id), str)
        self.assertTrue(type(U.created_at) is datetime.datetime)
        self.assertTrue(type(U.updated_at) is datetime.datetime)
        self.assertEqual(type(U.name), str)

    def test_Amenity_diff_id(self):
        """Test Amenity instance different id"""
        U1 = Amenity()
        U2 = Amenity()
        U3 = Amenity()
        self.assertNotEqual(U1.id, U2.id)
        self.assertNotEqual(U1.id, U3.id)
        self.assertNotEqual(U2.id, U3.id)

    def test_Amenity_str(self):
        """Test Amenity print"""
        U = Amenity()
        s = "[Amenity] ({}) {}".format(U.id, U.__dict__)
        self.assertEqual(s, str(U))

    def test_Amenity_none_kwargs(self):
        """Test Amenity none kwargs"""
        with self.assertRaises(TypeError):
            Amenity(id=None, created_at=None, updated_at=None)

    def test_Amenity_kwargs(self):
        """Test Amenity kwargs"""
        U1 = Amenity()
        U1.name = "Holberton"
        dict = U1.to_dict()
        U2 = Amenity(**dict)
        self.assertEqual(U1.id, U1.id)
        self.assertEqual(U1.created_at, U2.created_at)
        self.assertEqual(U1.updated_at, U2.updated_at)
        self.assertEqual(U1.name, U2.name)
        self.assertNotEqual(U1, U2)

    def test_amenity_save_none(self):
        """Tests save no instances"""
        with self.assertRaises(TypeError):
            Amenity.save()

    def test_amenity_save(self):
        """Tests save"""
        U = Amenity()
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
            Amenity.save(self, 1, "Hello")


if __name__ == '__main__':
    unittest.main()
