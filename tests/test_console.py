#!/usr/bin/python3
"""a inittest for the consol module
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

    # def test_create_existing_class_saved(self):
    #     with patch("sys.stdout", new=StringIO()) as f:
    #         for class_name, class_type in self.class_mapping.items():
    #             HBNBCommand().onecmd(f"create {class_name}")
    #             output = f.getvalue().strip()
    #             self.assertTrue(output)
    #             self.assertIn(f"{class_name}.{output}", storage.all().keys())

    # def test_create_existing_class_has_id(self):
    #     with patch("sys.stdout", new=StringIO()) as f:
    #         for class_name, class_type in self.class_mapping.items():
    #             HBNBCommand().onecmd(f"create {class_name}")
    #             output = f.getvalue().strip()
    #             self.assertTrue(output)
    #             obj_id = output
    #             self.assertIn(f"{class_name}.{obj_id}", storage.all().keys())

    # def test_create_existing_class_with_args_saved(self):
    #     with patch("sys.stdout", new=StringIO()) as f:
    #         for class_name, class_type in self.class_mapping.items():
    #             HBNBCommand().onecmd(f'create {class_name}')
    #             output = f.getvalue().strip()
    #             self.assertTrue(output)
    #             self.assertIn(f'{class_name}.' + output, storage.all().keys())

    # def test_create_existing_class_with_args_has_id(self):
    #     with patch("sys.stdout", new=StringIO()) as f:
    #         for class_name, class_type in self.class_mapping.items():
    #             HBNBCommand().onecmd(f'create {class_name} name="test" number=123')
    #             output = f.getvalue().strip()
    #             self.assertTrue(output)
    #             obj_id = output
    #             self.assertIn(f"{class_name}.{obj_id}", storage.all().keys())

    def test_create_non_existing_class_not_saved(self):
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("create NonExistingClass")
            output = f.getvalue().strip()
            self.assertEqual("** class doesn't exist **", output)
            self.assertNotIn("NonExistingClass", storage.all().keys())

    def test_create_non_existing_class_returns_error_message(self):
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("create NonExistingClass")
            output = f.getvalue().strip()
            self.assertEqual("** class doesn't exist **", output)

    def test_create_existing_class_invalid_args_not_saved(self):
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd('create BaseModel name=test number="invalid"')
            output = f.getvalue().strip()
            self.assertTrue(re.match(r'^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$', output))
            self.assertNotIn("BaseModel", storage.all().keys())

    # def test_create_existing_class_has_created_at(self):
    #     with patch("sys.stdout", new=StringIO()) as f:
    #         for class_name, class_type in self.class_mapping.items():
    #             HBNBCommand().onecmd(f"create {class_name}")
    #             output = f.getvalue().strip()
    #             self.assertTrue(output)
    #             obj_id = output
    #             key = f"{class_name}.{obj_id}"
    #             self.assertIn(key, storage.all().keys())
    #             self.assertIn("created_at", storage.all()[key].to_dict())

    # def test_create_existing_class_has_updated_at(self):
    #     with patch("sys.stdout", new=StringIO()) as f:
    #         for class_name, class_type in self.class_mapping.items():
    #             HBNBCommand().onecmd(f"create {class_name}")
    #             output = f.getvalue().strip()
    #             self.assertTrue(output)
    #             obj_id = output
    #             key = f"{class_name}.{obj_id}"
    #             self.assertIn(key, storage.all().keys())
    #             self.assertIn("updated_at", storage.all()[key].to_dict())

    # def test_create_existing_class_has_to_dict(self):
    #     with patch("sys.stdout", new=StringIO()) as f:
    #         for class_name, class_type in self.class_mapping.items():
    #             HBNBCommand().onecmd(f"create {class_name}")
    #             output = f.getvalue().strip()
    #             self.assertTrue(output)
    #             obj_id = output
    #             key = f"{class_name}.{obj_id}"
    #             self.assertIn(key, storage.all().keys())
    #             self.assertTrue(hasattr(storage.all()[key], "to_dict"))

    def test_destroy_BaseModel_no_instance_id(self):
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("destroy BaseModel")
            expected_output = "** instance id missing **"
            self.assertEqual(expected_output, f.getvalue().strip())

    def test_destroy_BaseModel_save_change(self):
        storage = FileStorage()
        storage.reload()
        with patch("sys.stdout", new=StringIO()) as f:
            for class_name, class_type in self.class_mapping.items():
                HBNBCommand().onecmd(f"create {class_name}")
                obj_id = f.getvalue().strip()
                HBNBCommand().onecmd(f"destroy {class_name} {obj_id}")
                self.assertNotIn(obj_id, storage.all())

    def test_destroy_BaseModel_returns_none(self):
        with patch("sys.stdout", new=StringIO()) as f:
            result = HBNBCommand().onecmd("destroy BaseModel")
            self.assertIsNone(result)

    def test_destroy_BaseModel_prints_nothing(self):
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("destroy BaseModel")
            self.assertEqual("** instance id missing **", f.getvalue().strip())

    def test_destroy_BaseModel_no_exceptions(self):
        try:
            HBNBCommand().onecmd("destroy BaseModel")
        except Exception as e:
            self.fail(f"do_destroy raised an exception: {e}")

    def test_destroy_no_class_name(self):
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("destroy")
            expected_output = "** class name missing **"
            self.assertEqual(expected_output, f.getvalue().strip())

    def test_destroy_invalid_class_name_(self):
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("destroy InvalidClass")
            expected_output = "** class doesn't exist **"
            self.assertEqual(expected_output, f.getvalue().strip())

    def test_destroy_BaseModel_missing_instance_id_(self):
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("destroy BaseModel")
            expected_output = "** instance id missing **"
            self.assertEqual(expected_output, f.getvalue().strip())

    def test_destroy_BaseModel_no_instance_found_(self):
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("destroy BaseModel 12345")
            expected_output = "** no instance found **"
            self.assertEqual(expected_output, f.getvalue().strip())

    def test_destroy_BaseModel_instance_found_deletes_from_storage(self):
        with patch("sys.stdout", new=StringIO()) as f:
            for class_name, class_type in self.class_mapping.items():
                HBNBCommand().onecmd(f"create {class_name}")
                obj_id = f.getvalue().strip()
                HBNBCommand().onecmd(f"destroy {class_name} {obj_id}")
                self.assertNotIn(obj_id, storage.all())

    def test_destroy_BaseModel_instance_found_saves_change(self):
        with patch("sys.stdout", new=StringIO()) as f:
            for class_name, class_type in self.class_mapping.items():
                HBNBCommand().onecmd(f"create {class_name}")
                obj_id = f.getvalue().strip()
                HBNBCommand().onecmd(f"destroy {class_name} {obj_id}")
                storage.reload()
                self.assertNotIn(obj_id, storage.all())

    def test_destroy_valid_class_name_and_id_with_numbers(self):
        with patch("sys.stdout", new=StringIO()) as f:
            for class_name, class_type in self.class_mapping.items():
                HBNBCommand().onecmd(f"create {class_name}")
                obj_id = f.getvalue().strip()
                HBNBCommand().onecmd(f"destroy {class_name} '{obj_id}12345'")
                storage.reload()
                self.assertNotIn(obj_id, storage.all())

    def test_destroy_valid_class_name_and_id_with_special_characters(self):
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
