#!/usr/bin/python3
"""
Console Unittest Module
"""
import unittest
from console import HBNBCommand
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.state import State
from models import storage
from unittest.mock import patch
from io import StringIO
import os
import pep8


class TestHBNBCommand(unittest.TestCase):
    """Tests HBNBCommand Console"""

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
        result = style.check_files(['models/amenity.py'])
        self.assertEqual(result.total_errors, 0, "Fix pep8")

    def test_HBNBCommand_help(self):
        """Tests the help command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help")
        string = """
Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update

"""
        self.assertEqual(string, f.getvalue())

    def test_HBNBCommand_help_EOF(self):
        """Tests the help EOF command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help EOF")
        string = "EOF command to exit the program\n"
        self.assertEqual(string, f.getvalue())

    def test_HBNBCommand_help_all(self):
        """Tests the help all command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help all")
        string = "All command prints all string representation of \
all instances\n"
        self.assertEqual(string, f.getvalue())

    def test_HBNBCommand_help_count(self):
        """Tests the help count command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help count")
        string = "Count command counts the instances of a class\n"
        self.assertEqual(string, f.getvalue())

    def test_HBNBCommand_help_create(self):
        """Tests the help count command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help create")
        string = "Create command new instance\n"
        self.assertEqual(string, f.getvalue())

    def test_HBNBCommand_help_destroy(self):
        """Tests the help destroy command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help destroy")
        string = "Destroy command to delete a instance\n"
        self.assertEqual(string, f.getvalue())

    def test_HBNBCommand_help_quit(self):
        """Tests the help quit command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help quit")
        string = "Quit command to exit the program\n"
        self.assertEqual(string, f.getvalue())

    def test_HBNBCommand_help_show(self):
        """Tests the help show command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help show")
        string = "Show command display info of the id instance\n"
        self.assertEqual(string, f.getvalue())

    def test_HBNBCommand_help_update(self):
        """Tests the help update command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help update")
        string = "Update command load new info at the instances\n"
        self.assertEqual(string, f.getvalue())

    def test_HBNBCommand_create_error1(self):
        """Tests the create error 1"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create")
        string = "** class name missing **\n"
        self.assertEqual(string, f.getvalue())

    def test_HBNBCommand_create_error2(self):
        """Tests the create error 2"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create pepito")
        string = "** class doesn't exist **\n"
        self.assertEqual(string, f.getvalue())

    def test_HBNBCommand_destroy_error1(self):
        """Tests the destroy error 1"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy")
        string = "** class name missing **\n"
        self.assertEqual(string, f.getvalue())

    def test_HBNBCommand_destroy_error2(self):
        """Tests the destroy error 2"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy pepito")
        string = "** class doesn't exist **\n"
        self.assertEqual(string, f.getvalue())

    def test_HBNBCommand_destroy_error3(self):
        """Tests the destroy error 3"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy BaseModel")
        string = "** instance id missing **\n"
        self.assertEqual(string, f.getvalue())

    def test_HBNBCommand_show_error1(self):
        """Tests the show error 1"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show")
        string = "** class name missing **\n"
        self.assertEqual(string, f.getvalue())

    def test_HBNBCommand_show_error2(self):
        """Tests the show error 2"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show pepito")
        string = "** class doesn't exist **\n"
        self.assertEqual(string, f.getvalue())

    def test_HBNBCommand_show_error3(self):
        """Tests the show error 3"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show BaseModel")
        string = "** instance id missing **\n"
        self.assertEqual(string, f.getvalue())

    def test_HBNBCommand_show_error4(self):
        """Tests the show error 4"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show BaseModel 123")
        string = "** no instance found **\n"
        self.assertEqual(string, f.getvalue())

    def test_HBNBCommand_all_error1(self):
        """Tests the all error 1"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all pepito")
        string = "** class doesn't exist **\n"
        self.assertEqual(string, f.getvalue())

    def test_HBNBCommand_update_error1(self):
        """Tests the update error 1"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update")
        string = "** class name missing **\n"
        self.assertEqual(string, f.getvalue())

    def test_HBNBCommand_update_error2(self):
        """Tests the update error 2"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update pepito")
        string = "** class doesn't exist **\n"
        self.assertEqual(string, f.getvalue())

    def test_HBNBCommand_update_error3(self):
        """Tests the update error 3"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update BaseModel")
        string = "** instance id missing **\n"
        self.assertEqual(string, f.getvalue())

    def test_HBNBCommand_update_error4(self):
        """Tests the update error 4"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update BaseModel 1234")
        string = "** attribute name missing **\n"
        self.assertEqual(string, f.getvalue())

    def test_HBNBCommand_update_error5(self):
        """Tests the update error 5"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update BaseModel 1234 name")
        string = "** value missing **\n"
        self.assertEqual(string, f.getvalue())

    def test_HBNBCommand_update_error6(self):
        """Tests the update error 6"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update BaseModel 1234 name Juan")
        string = "** no instance found **\n"
        self.assertEqual(string, f.getvalue())

    def test_HBNBCommand_create(self):
        """Tests the create"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            HBNBCommand().onecmd("create User")
            HBNBCommand().onecmd("create State")
            HBNBCommand().onecmd("create City")
            HBNBCommand().onecmd("create Place")
            HBNBCommand().onecmd("create Amenity")
            HBNBCommand().onecmd("create Review")
        self.assertEqual(7, len(storage.all()))


if __name__ == "__main__":
    unittest.main()
