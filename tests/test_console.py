#!/usr/bin/python3
"""a inittest for the consol module
"""
import unittest
from console import HBNBCommand
from models import FileStorage
from models import storage
from io import StringIO
from models.base_model import BaseModel
from unittest.mock import patch


class TestHBNBCommand(unittest.TestCase):

    # tests for the create methode
    # -------------------------------------------------------------------
    # Create an instance of an existing class and verify that it was saved
    def test_do_create_existing_class_saved(self):
        """
        Test that do_create saves an instance of an existing class
        """
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            output = f.getvalue().strip()
            self.assertTrue(output)
            self.assertIn(f"BaseModel.{output}", storage.all().keys())

    # Create an instance of an existing class and verify that it has an id
    def test_do_create_existing_class_has_id(self):
        """
        Test that do_create assigns an id to an instance of an existing class
        """
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            output = f.getvalue().strip()
            self.assertTrue(output)
            obj_id = output
            self.assertIn(f"BaseModel.{obj_id}", storage.all().keys())

    # Create an instance of an existing class with
    # arguments and verify that it was saved
    def test_do_create_existing_class_with_args_saved(self):
        """
        Test that do_create saves an instance of
        an existing class with arguments
        """
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd('create BaseModel')
            output = f.getvalue().strip()
            self.assertTrue(output)
            self.assertIn('BaseModel.' + output, storage.all().keys())

    # Create an instance of an existing class with
    # arguments and verify that it has an id
    def test_do_create_existing_class_with_args_has_id(self):
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd('create BaseModel name="test" number=123')
            output = f.getvalue().strip()
            self.assertTrue(output)
            obj_id = output
            self.assertIn(f"BaseModel.{obj_id}", storage.all().keys())

    # tests for the destroy methode
    # ---------------------------------------------------------
    # Deletes an instance based on the class name
    # and id when no instance id is provided.

    def test_do_destroy_BaseModel_no_instance_id(self):
        """
        Test that do_destroy deletes an instance based on the class name and id
        when no instance id is provided
        """
        from unittest.mock import patch
        from io import StringIO

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("destroy BaseModel")
            expected_output = "** instance id missing **"
            self.assertEqual(expected_output, f.getvalue().strip())

    # Saves the change into the JSON file.
    def test_do_destroy_BaseModel_save_change(self):
        """
        Test that do_destroy saves the change into the JSON file
        """
        storage = FileStorage()
        storage.reload()
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            obj_id = f.getvalue().strip()
            HBNBCommand().onecmd(f"destroy BaseModel {obj_id}")
            self.assertNotIn(obj_id, storage.all())

    # The test checks if the do_destroy method returns None.
    def test_do_destroy_BaseModel_returns_none(self):
        """
        Test that do_destroy returns None
        """
        with patch("sys.stdout", new=StringIO()) as f:
            result = HBNBCommand().onecmd("destroy BaseModel")
            self.assertIsNone(result)

    # Test that do_destroy prints nothing.
    def test_do_destroy_BaseModel_prints_nothing(self):
        """
        Test that do_destroy prints nothing when no instance id given
        """
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("destroy BaseModel")
            self.assertEqual("** instance id missing **", f.getvalue().strip())

    # Does not raise any exceptions.
    def test_do_destroy_BaseModel_no_exceptions(self):
        """
        Test that do_destroy does not raise any exceptions
        """
        try:
            HBNBCommand().onecmd("destroy BaseModel")
        except Exception as e:
            self.fail(f"do_destroy raised an exception: {e}")

    # If no arguments are passed, prints "**
    # class name missing **".
    def test_do_destroy_no_class_name(self):
        """
        Test that do_destroy prints "** class name missing **"
        if no arguments are passed
        """
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("destroy")
            expected_output = "** class name missing **"
            self.assertEqual(expected_output, f.getvalue().strip())
    # If the class name does not exist, prints "**
    # class doesn't exist **".

    def test_do_destroy_invalid_class_name_(self):
        """
        Test that do_destroy prints "** class doesn't exist **"
        if the class name does not exist
        """
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("destroy InvalidClass")
            expected_output = "** class doesn't exist **"
            self.assertEqual(expected_output, f.getvalue().strip())

        # If the instance id is missing, prints "** instance id missing **".
    def test_do_destroy_BaseModel_missing_instance_id_(self):
        """
        Test that do_destroy prints "** instance id missing **"
        if the instance id is missing
        """
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("destroy BaseModel")
            expected_output = "** instance id missing **"
            self.assertEqual(expected_output, f.getvalue().strip())

        # If no instance is found, prints "** no instance found **".
    def test_do_destroy_BaseModel_no_instance_found_(self):
        """
        Test that do_destroy prints "** no instance found **"
        if no instance is found
        """
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("destroy BaseModel 12345")
            expected_output = "** no instance found **"
            self.assertEqual(expected_output, f.getvalue().strip())

        # If the instance is found,
        # deletes it from the storage.
    def test_do_destroy_BaseModel_instance_found_deletes_from_storage(self):
        """
        Test that do_destroy deletes the
        instance from the storage if it is found
        """
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            obj_id = f.getvalue().strip()
            HBNBCommand().onecmd(f"destroy BaseModel {obj_id}")
            self.assertNotIn(obj_id, storage.all())

    # If the instance is found,
    # saves the change into the JSON file.
    def test_do_destroy_BaseModel_instance_found_saves_change(self):
        """
        Test that do_destroy saves the change
        into the JSON file if the instance is found
        """
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            obj_id = f.getvalue().strip()
            HBNBCommand().onecmd(f"destroy BaseModel {obj_id}")
            storage.reload()
            self.assertNotIn(obj_id, storage.all())

        # Deletes an instance when given
        # a valid class name and id with numbers.
    def test_do_destroy_valid_class_name_and_id_with_numbers(self):
        """
        Test that do_destroy deletes an instance when
        given a valid class name and id with numbers
        """
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            obj_id = f.getvalue().strip()
            HBNBCommand().onecmd(f"destroy BaseModel '{obj_id}12345'")
            storage.reload()
            self.assertNotIn(obj_id, storage.all())

    # Deletes an instance when given a valid
    # class name and id with special characters.
    def test_do_destroy_valid_class_name_and_id_with_special_characters(self):
        """
        Test that do_destroy deletes an instance when given
        a valid class name and id with special characters
        """
        storage = FileStorage()
        storage.reload()
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            obj_id = f.getvalue().strip()
            HBNBCommand().onecmd(f"destroy BaseModel '{obj_id}!@#$%^&*()'")
            storage.reload()
            self.assertNotIn(obj_id, storage.all())

    def test_do_show_valid_class_name_and_instance_id(self):
        """When given a valid class name and instance id, it should
        print the string representation of the instance."""
        base_model = BaseModel()
        base_model.id = "123"
        storage.all()["BaseModel.123"] = base_model
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().do_show("BaseModel 123")
            instance_str = output.getvalue().strip()
            self.assertEqual(instance_str, str(storage.all()["BaseModel.123"]))

    def test_do_show_invalid_class_name(self):
        """# When given an invalid class name
        it should print an error message.
        """
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().do_show("InvalidClass 123")
            error_msg = output.getvalue().strip()
            self.assertEqual(error_msg, "** class doesn't exist **")

    def test_do_show_invalid_instance_id(self):
        """# When given an invalid instance id
        it should print an error message.
        """
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().do_show("BaseModel InvalidID")
            error_msg = output.getvalue().strip()
            self.assertEqual(error_msg, "** no instance found **")

    def test_do_show_invalid_class_name_and_instance_id(self):
        """# When given an invalid class name and instance id
        it should print an error message.
        """
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().do_show("InvalidClass InvalidID")
            error_msg = output.getvalue().strip()
            self.assertEqual(error_msg, "** class doesn't exist **")

    def test_do_all_no_arguments(self):
        """# When called with no arguments
        it should print all string representations of all instances.
        """
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().do_all("")
            output = f.getvalue().strip()

            formatted_objects = []
            for obj in storage.all().values():
                formatted_objects.append(f"[{str(obj)} {obj.to_dict()}]")
            for formatted_obj in formatted_objects:
                self.assertIn(formatted_obj, output)

    def test_do_all_valid_class_name_with_patch(self):
        """When called with a valid class name as an
        argument, it should print all string representations
        of all instances of that class.
        """
        from unittest.mock import patch
        from io import StringIO

        with patch("sys.stdout", new=StringIO()) as f:
            with patch("unittest.mock.patch") as mock_patch:
                mock_patch.return_value = f
                HBNBCommand().do_all("BaseModel")
                output = f.getvalue().strip()

                formatted_objects = []
                for ob in storage.all().values():
                    if ob.__class__.__name__ == "BaseModel":
                        formatted_objects.append(f"[{str(ob)} {ob.to_dict()}]")
                for formatted_obj in formatted_objects:
                    self.assertIn(formatted_obj, output)

    def test_calls_do_all(self):
        """calls do_all method if 'class.all()' is in the command
        """
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.all()")
            self.assertIn("[BaseModel", f.getvalue().strip())


if __name__ == "__main__":
    unittest.main()
