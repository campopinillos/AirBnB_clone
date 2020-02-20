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


if __name__ == "__main__":
    unittest.main()
