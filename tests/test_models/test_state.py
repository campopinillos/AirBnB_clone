#!/usr/bin/python3
"""
State Unittest Module
"""
import unittest
from models.base_model import BaseModel
from models.state import State
from models.engine.file_storage import FileStorage
import os
import pep8
import json
import datetime


class TestState(unittest.TestCase):
    """State Class Tests"""

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
        result = style.check_files(['models/state.py'])
        self.assertEqual(result.total_errors, 0, "Fix pep8")

    def test_subclass_State(self):
        """Test State instance"""
        self.assertTrue(issubclass(State, BaseModel))

    def test_State_basic_instance(self):
        """Test State instance"""
        A = State()
        A.name = "State"
        self.assertIsInstance(A, BaseModel)
        self.assertEqual(State, type(A))
        self.assertTrue(hasattr(A, "created_at"))
        self.assertTrue(hasattr(A, "updated_at"))
        self.assertTrue(hasattr(A, "name"))

    def test_State_basic_instance_none(self):
        """Test State instance None"""
        with self.assertRaises(TypeError):
            State(None)

    def test_State_attr_types(self):
        """Test State instance attributes"""
        U = State()
        U.name = "State"
        self.assertEqual(type(U.id), str)
        self.assertTrue(type(U.created_at) is datetime.datetime)
        self.assertTrue(type(U.updated_at) is datetime.datetime)
        self.assertEqual(type(U.name), str)

    def test_State_diff_id(self):
        """Test State instance different id"""
        U1 = State()
        U2 = State()
        U3 = State()
        self.assertNotEqual(U1.id, U2.id)
        self.assertNotEqual(U1.id, U3.id)
        self.assertNotEqual(U2.id, U3.id)

    def test_State_str(self):
        """Test State print"""
        U = State()
        s = "[State] ({}) {}".format(U.id, U.__dict__)
        self.assertEqual(s, str(U))

    def test_State_none_kwargs(self):
        """Test State none kwargs"""
        with self.assertRaises(TypeError):
            State(id=None, created_at=None, updated_at=None)

    def test_State_kwargs(self):
        """Test State kwargs"""
        U1 = State()
        U1.name = "State"
        dict = U1.to_dict()
        U2 = State(**dict)
        self.assertEqual(U1.id, U1.id)
        self.assertEqual(U1.created_at, U2.created_at)
        self.assertEqual(U1.updated_at, U2.updated_at)
        self.assertEqual(U1.name, U2.name)
        self.assertNotEqual(U1, U2)

    def test_State_save_none(self):
        """Tests save no instances"""
        with self.assertRaises(TypeError):
            State.save()

    def test_State_save(self):
        """Tests save"""
        U = State()
        U.name = "State"
        U.save()
        k = "{}.{}".format(type(U).__name__, U.id)
        dict = {k: U.to_dict()}
        self.assertTrue(os.path.isfile(FileStorage._FileStorage__file_path))
        with open(FileStorage._FileStorage__file_path,
                  "r", encoding="utf-8") as file:
            self.assertEqual(json.load(file), dict)


if __name__ == '__main__':
    unittest.main()
