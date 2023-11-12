#!/usr/bin/python3
"""Unit tests for the console module
"""
import unittest
import re
from console import HBNBCommand
from models import FileStorage
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from io import StringIO
from unittest.mock import patch

class TestHBNBCommand(unittest.TestCase):

    class_mapping = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review
    }

    def test_create_non_existing_class_not_saved(self):
        """Test if creating an instance of a non-existing class does not save it"""
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("create NonExistingClass")
            output = f.getvalue().strip()
            self.assertEqual("** class doesn't exist **", output)
            self.assertNotIn("NonExistingClass", storage.all().keys())

    def test_create_non_existing_class_returns_error_message(self):
        """Test if creating an instance of a non-existing class returns an error message"""
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("create NonExistingClass")
            output = f.getvalue().strip()
            self.assertEqual("** class doesn't exist **", output)

    def test_create_existing_class_invalid_args_not_saved(self):
        """Test if creating an instance with invalid arguments does not save it"""
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd('create BaseModel name=test number="invalid"')
            output = f.getvalue().strip()
            self.assertTrue(re.match(r'^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$', output))
            self.assertNotIn("BaseModel", storage.all().keys())

    def test_destroy_BaseModel_no_instance_id(self):
        """Test if destroy command without instance id returns the correct error message"""
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("destroy BaseModel")
            expected_output = "** instance id missing **"
            self.assertEqual(expected_output, f.getvalue().strip())

    def test_destroy_BaseModel_save_change(self):
        """Test if destroy command saves the change in storage"""
        storage = FileStorage()
        storage.reload()
        with patch("sys.stdout", new=StringIO()) as f:
            for class_name, class_type in self.class_mapping.items():
                HBNBCommand().onecmd(f"create {class_name}")
                obj_id = f.getvalue().strip()
                HBNBCommand().onecmd(f"destroy {class_name} {obj_id}")
                self.assertNotIn(obj_id, storage.all())

    def test_destroy_BaseModel_returns_none(self):
        """Test if destroy command returns None"""
        with patch("sys.stdout", new=StringIO()) as f:
            result = HBNBCommand().onecmd("destroy BaseModel")
            self.assertIsNone(result)

    def test_destroy_BaseModel_prints_nothing(self):
        """Test if destroy command without instance id prints the correct error message"""
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("destroy BaseModel")
            self.assertEqual("** instance id missing **", f.getvalue().strip())

    def test_destroy_BaseModel_no_exceptions(self):
        """Test if destroy command for BaseModel does not raise exceptions"""
        try:
            HBNBCommand().onecmd("destroy BaseModel")
        except Exception as e:
            self.fail(f"do_destroy raised an exception: {e}")

    def test_destroy_no_class_name(self):
        """Test if destroy command without class name returns the correct error message"""
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("destroy")
            expected_output = "** class name missing **"
            self.assertEqual(expected_output, f.getvalue().strip())

    def test_destroy_invalid_class_name_(self):
        """Test if destroy command with invalid class name returns the correct error message"""
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("destroy InvalidClass")
            expected_output = "** class doesn't exist **"
            self.assertEqual(expected_output, f.getvalue().strip())

    def test_destroy_BaseModel_missing_instance_id_(self):
        """Test if destroy command without instance id for BaseModel returns the correct error message"""
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("destroy BaseModel")
            expected_output = "** instance id missing **"
            self.assertEqual(expected_output, f.getvalue().strip())

    def test_destroy_BaseModel_no_instance_found_(self):
        """Test if destroy command with no instance found for BaseModel returns the correct error message"""
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("destroy BaseModel 12345")
            expected_output = "** no instance found **"
            self.assertEqual(expected_output, f.getvalue().strip())

    def test_destroy_BaseModel_instance_found_deletes_from_storage(self):
        """Test if destroy command deletes the instance from storage if found"""
        with patch("sys.stdout", new=StringIO()) as f:
            for class_name, class_type in self.class_mapping.items():
                HBNBCommand().onecmd(f"create {class_name}")
                obj_id = f.getvalue().strip()
                HBNBCommand().onecmd(f"destroy {class_name} {obj_id}")
                self.assertNotIn(obj_id, storage.all())

    def test_destroy_BaseModel_instance_found_saves_change(self):
        """Test if destroy command saves the change in storage if instance is found"""
        with patch("sys.stdout", new=StringIO()) as f:
            for class_name, class_type in self.class_mapping.items():
                HBNBCommand().onecmd(f"create {class_name}")
                obj_id = f.getvalue().strip()
                HBNBCommand().onecmd(f"destroy {class_name} {obj_id}")
                storage.reload()
                self.assertNotIn(obj_id, storage.all())

    def test_destroy_valid_class_name_and_id_with_numbers(self):
        """Test if destroy command with valid class name and id containing numbers works"""
        with patch("sys.stdout", new=StringIO()) as f:
            for class_name, class_type in self.class_mapping.items():
                HBNBCommand().onecmd(f"create {class_name}")
                obj_id = f.getvalue().strip()
                HBNBCommand().onecmd(f"destroy {class_name} '{obj_id}12345'")
                storage.reload()
                self.assertNotIn(obj_id, storage.all())

    def test_destroy_valid_class_name_and_id_with_special_characters(self):
        """Test if destroy command with valid class name and id containing special characters works"""
        storage = FileStorage()
        storage.reload()
        with patch("sys.stdout", new=StringIO()) as f:
            for class_name, class_type in self.class_mapping.items():
                HBNBCommand().onecmd(f"create {class_name}")
                obj_id = f.getvalue().strip()
                HBNBCommand().onecmd(f"destroy {class_name} '{obj_id}!@#$%^&*()'")
                storage.reload()
                self.assertNotIn(obj_id, storage.all())

if __name__ == "__main__":
    unittest.main()
