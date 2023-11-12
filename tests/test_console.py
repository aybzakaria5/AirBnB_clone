#!/usr/bin/python3
"""a test for the consol"""
import unittest
from models import storage
import os
from unittest.mock import patch
from console import HBNBCommand
from io import StringIO
from models.engine.file_storage import FileStorage


class CreateTest(unittest.TestCase):
    """Create command"""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "Thefile.json")
        except IOError:
            pass
        FileStorage.__objects = {}

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("Thefile.json", "file.json")
        except IOError:
            pass

    def test_create_no_class(self):
        """no class given"""
        with patch("sys.stdout", new=StringIO()) as op:
            HBNBCommand().onecmd("create")
            expected = "** class name missing **"
            self.assertEqual(expected, op.getvalue().strip())

    def test_create_no_existing_class(self):
        """Test create with class doesn't exist"""
        with patch("sys.stdout", new=StringIO()) as op:
            HBNBCommand().onecmd("create Cake")
            expected = "** class doesn't exist **"
            self.assertEqual(expected, op.getvalue().strip())

    def test_create_BaseModel_instance(self):
        """Test create BaseModel"""
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create BaseModel")
            with open("file.json", "r") as file:
                self.assertIn(output.getvalue().strip(), file.read())

    def test_create_User_instance(self):
        """Test create User"""
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create User")
            with open("file.json", "r") as file:
                self.assertIn(output.getvalue().strip(), file.read())

    def test_create_Amenity_instance(self):
        """Test create Amenity"""
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Amenity")
            with open("file.json", "r") as file:
                self.assertIn(output.getvalue().strip(), file.read())

    def test_create_City_instance(self):
        """Test create City"""
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create City")
            with open("file.json", "r") as file:
                self.assertIn(output.getvalue().strip(), file.read())

    def test_create_Place_instance(self):
        """Test create Place"""
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Place")
            with open("file.json", "r") as file:
                self.assertIn(output.getvalue().strip(), file.read())

    def test_create_Review_instance(self):
        """Test create Review"""
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Review")
            with open("file.json", "r") as file:
                self.assertIn(output.getvalue().strip(), file.read())

    def test_create_State_instance(self):
        """Test create State"""
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create State")
            with open("file.json", "r") as file:
                self.assertIn(output.getvalue().strip(), file.read())

   
if __name__ == '__main__':
    unittest.main()
