#!/usr/bin/python3
"""
Review Unittest Module
"""
import unittest
from models.base_model import BaseModel
from models.review import Review
from models.engine.file_storage import FileStorage
import os
import pep8
import json
import datetime


class TestReview(unittest.TestCase):
    """Review Class Tests"""

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
        result = style.check_files(['models/review.py'])
        self.assertEqual(result.total_errors, 0, "fix pep8")

    def test_subclass_Review(self):
        """Test Review instance"""
        self.assertTrue(issubclass(Review, BaseModel))

    def test_Review_basic_instance(self):
        """Test Review instance"""
        A = Review()
        self.assertIsInstance(A, BaseModel)
        self.assertEqual(Review, type(A))
        self.assertTrue(hasattr(A, "created_at"))
        self.assertTrue(hasattr(A, "updated_at"))
        self.assertTrue(hasattr(A, "place_id"))
        self.assertTrue(hasattr(A, "user_id"))
        self.assertTrue(hasattr(A, "text"))

    def test_Review_basic_instance_none(self):
        """Test Review instance None"""
        with self.assertRaises(TypeError):
            Review(None)

    def test_Review_attr_types(self):
        """Test Review instance attributes"""
        U = Review()
        self.assertEqual(type(U.id), str)
        self.assertTrue(type(U.created_at) is datetime.datetime)
        self.assertTrue(type(U.updated_at) is datetime.datetime)
        self.assertEqual(type(U.place_id), str)
        self.assertEqual(type(U.user_id), str)
        self.assertEqual(type(U.text), str)

    def test_Review_diff_id(self):
        """Test Review instance different id"""
        U1 = Review()
        U2 = Review()
        U3 = Review()
        self.assertNotEqual(U1.id, U2.id)
        self.assertNotEqual(U1.id, U3.id)
        self.assertNotEqual(U2.id, U3.id)

    def test_Review_str(self):
        """Test Review print"""
        U = Review()
        s = "[Review] ({}) {}".format(U.id, U.__dict__)
        self.assertEqual(s, str(U))

    def test_Review_none_kwargs(self):
        """Test Review none kwargs"""
        with self.assertRaises(TypeError):
            Review(id=None, created_at=None, updated_at=None)

    def test_Review_kwargs(self):
        """Test Review kwargs"""
        U1 = Review()
        dict = U1.to_dict()
        U2 = Review(**dict)
        self.assertEqual(U1.id, U1.id)
        self.assertEqual(U1.created_at, U2.created_at)
        self.assertEqual(U1.updated_at, U2.updated_at)
        self.assertNotEqual(U1, U2)

    def test_Review_save_none(self):
        """Tests save no instances"""
        with self.assertRaises(TypeError):
            Review.save()

    def test_Review_save(self):
        """Tests save"""
        U = Review()
        U.save()
        k = "{}.{}".format(type(U).__name__, U.id)
        dict = {k: U.to_dict()}
        self.assertTrue(os.path.isfile(FileStorage._FileStorage__file_path))
        with open(FileStorage._FileStorage__file_path,
                  "r", encoding="utf-8") as file:
            self.assertEqual(json.load(file), dict)


if __name__ == '__main__':
    unittest.main()
