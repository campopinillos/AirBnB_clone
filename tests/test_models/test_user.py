#!/U/bin/python3
"""
User Unittest Module
"""
import unittest
from models.base_model import BaseModel
from models.user import User
from models.engine.file_storage import FileStorage
import os
import pep8
import json
import datetime


class TestUser(unittest.TestCase):
    """User Class Tests"""

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
        result = style.check_files(['models/user.py'])
        self.assertEqual(result.total_errors, 0, "fix pep8")

    def test_subclass_user(self):
        """Test user instance"""
        self.assertTrue(issubclass(User, BaseModel))
        self.assertEqual(str(type(User())), "<class 'models.user.User'>")
        self.assertIsInstance(User(), User)

    def test_user_basic_instance(self):
        """Test user instance"""
        U = User()
        U.email = "123@mail.com"
        U.password = "123"
        U.first_name = "Betty"
        U.last_name = "Holberton"
        self.assertIsInstance(U, User)
        self.assertEqual(User, type(U))
        self.assertTrue(hasattr(U, "id"))
        self.assertTrue(hasattr(U, "created_at"))
        self.assertTrue(hasattr(U, "updated_at"))
        self.assertTrue(hasattr(U, "email"))
        self.assertTrue(hasattr(U, "password"))
        self.assertTrue(hasattr(U, "first_name"))
        self.assertTrue(hasattr(U, "last_name"))

    def test_user_basic_instance_none(self):
        """Test user instance None"""
        with self.assertRaises(TypeError):
            User(None)

    def test_user_attr_types(self):
        """Test user instance attributes"""
        U = User()
        U.email = "123@mail.com"
        U.password = "123"
        U.first_name = "Betty"
        U.last_name = "Holberton"
        self.assertTrue(type(U.id) is str)
        self.assertTrue(type(U.created_at) is datetime.datetime)
        self.assertTrue(type(U.updated_at) is datetime.datetime)
        self.assertTrue(type(U.email) is str)
        self.assertTrue(type(U.password) is str)
        self.assertTrue(type(U.first_name) is str)
        self.assertTrue(type(U.last_name) is str)

    def test_user_diff_id(self):
        """Test user instance different id"""
        U1 = User()
        U2 = User()
        U3 = User()
        self.assertNotEqual(U1.id, U2.id)
        self.assertNotEqual(U1.id, U3.id)
        self.assertNotEqual(U2.id, U3.id)

    def test_user_str(self):
        """Test user print"""
        U = User()
        s = "[User] ({}) {}".format(U.id, U.__dict__)
        self.assertEqual(s, str(U))

    def test_user_none_kwargs(self):
        """Test user none kwargs"""
        with self.assertRaises(TypeError):
            User(id=None, created_at=None, updated_at=None)

    def test_user_kwargs_to_dict(self):
        """Test user kwargs"""
        U1 = User()
        U1.email = "123@mail.com"
        U1.password = "123"
        U1.first_name = "Betty"
        U1.last_name = "Holberton"
        dict = U1.to_dict()
        U2 = User(**dict)
        self.assertEqual(U1.id, U1.id)
        self.assertEqual(U1.created_at, U2.created_at)
        self.assertEqual(U1.updated_at, U2.updated_at)
        self.assertEqual(U1.email, U2.email)
        self.assertEqual(U1.password, U2.password)
        self.assertEqual(U1.first_name, U2.first_name)
        self.assertEqual(U1.last_name, U2.last_name)
        self.assertNotEqual(U1, U2)

    def test_user_save_none(self):
        """Tests save no instances"""
        with self.assertRaises(TypeError):
            User.save()

    def test_user_save(self):
        """Tests save"""
        U = User()
        U.email = "123@mail.com"
        U.password = "123"
        U.first_name = "Betty"
        U.last_name = "Holberton"
        U.save()
        k = "{}.{}".format(type(U).__name__, U.id)
        dict = {k: U.to_dict()}
        self.assertTrue(os.path.isfile(FileStorage._FileStorage__file_path))
        with open(FileStorage._FileStorage__file_path,
                  "r", encoding="utf-8") as file:
            self.assertEqual(json.load(file), dict)

    def test_user_save_more_args(self):
        """Tests save with more arguments"""
        with self.assertRaises(TypeError):
            User.save(self, 1, "Hello")

    def test_user_docstring(self):
        """Test user docstring"""
        self.assertIsNotNone(User.__doc__)

    def test_user_to_dict(self):
        """ Test user to_dic """
        self.assertTrue('to_dict' in dir(User()))

    def test_user_save(self):
        """ Test save """
        B = User()
        B.save()
        self.assertNotEqual(B.created_at, B.updated_at)
        B.save()
        self.assertFalse(B.created_at == B.updated_at)

    def test_user_attributes_dict(self):
        U = User()
        U.email = "123@mail.com"
        U.password = "123"
        U.first_name = "Betty"
        U.last_name = "Holberton"
        self.assertTrue("id" in U.__dict__)
        self.assertTrue("email" in U.__dict__)
        self.assertTrue("password" in U.__dict__)
        self.assertTrue("first_name" in U.__dict__)
        self.assertTrue("last_name" in U.__dict__)
        self.assertTrue("created_at" in U.__dict__)
        self.assertTrue("updated_at" in U.__dict__)


if __name__ == '__main__':
    unittest.main()
