#!/usr/bin/python3
"""
Base Model Unittest Module
"""
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import os
import json
import datetime


class TestBaseModel(unittest.TestCase):
    """Base Model Class Tests"""

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

    def test_basemodel_basic_instance(self):
        """Test base model instance"""
        B = BaseModel()
        self.assertIsInstance(B, BaseModel)
        self.assertEqual(BaseModel, type(BaseModel()))
        self.assertTrue(hasattr(B, "id"))
        self.assertTrue(hasattr(B, "created_at"))
        self.assertTrue(hasattr(B, "updated_at"))

    def test_basemodel_basic_instance_none(self):
        """Test base model instance None"""
        with self.assertRaises(TypeError):
            BaseModel(None)

    def test_basemodel_attr_types(self):
        """Test base model instance attributes"""
        B = BaseModel()
        self.assertEqual(type(B.id), str)
        self.assertTrue(type(B.created_at) is datetime.datetime)
        self.assertTrue(type(B.updated_at) is datetime.datetime)

    def test_basemodel_diff_id(self):
        """Test base model instance different id"""
        B1 = BaseModel()
        B2 = BaseModel()
        B3 = BaseModel()
        self.assertNotEqual(B1.id, B2.id)
        self.assertNotEqual(B1.id, B3.id)
        self.assertNotEqual(B2.id, B3.id)

    def test_basemodel_str(self):
        """Test base model print"""
        B = BaseModel()
        s = "[BaseModel] ({}) {}".format(B.id, B.__dict__)
        self.assertEqual(s, str(B))

    def test_basemodel_none_kwargs(self):
        """Test base model none kwargs"""
        with self.assertRaises(TypeError):
            BaseModel(id=None, created_at=None, updated_at=None)

    def test_basemodel_kwargs_to_dict(self):
        """Test base model kwargs"""
        B1 = BaseModel()
        dict = B1.to_dict()
        B2 = BaseModel(**dict)
        self.assertEqual(B1.id, B1.id)
        self.assertEqual(B1.created_at, B2.created_at)
        self.assertEqual(B1.updated_at, B2.updated_at)
        self.assertNotEqual(B1, B2)

    def test_basemodel_save_none(self):
        """Tests save no instances"""
        with self.assertRaises(TypeError):
            BaseModel.save()

    def test_basemodel_save(self):
        """Tests save"""
        B = BaseModel()
        B.save()
        k = "{}.{}".format(type(B).__name__, B.id)
        dict = {k: B.to_dict()}
        self.assertTrue(os.path.isfile(FileStorage._FileStorage__file_path))
        with open(FileStorage._FileStorage__file_path,
                  "r", encoding="utf-8") as file:
            self.assertEqual(json.load(file), dict)

    def test_basemodel_save_more_args(self):
        """Tests save with more arguments"""
        with self.assertRaises(TypeError):
            BaseModel.save(self, 1, "Hello")


if __name__ == '__main__':
    unittest.main()
