#!/usr/bin/python
"""a unittest for the
console module
"""

import unittest

from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models import storage
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class TestHBNBCommand_methodes(unittest.TestCase):
    """testing all methodes wihtin hbnbnclass"""

    def test_create_existing_class(self):
        """create a class"""
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create BaseModel")
            obj_id = output.getvalue().strip()
            self.assertIsNotNone(storage.all()["BaseModel." + obj_id])

    def test_print_instance_id(self):
        """Print the ID of the newly created instance"""
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create BaseModel")
            obj_id = output.getvalue().strip()
            self.assertEqual(obj_id, storage.all()["BaseModel." + obj_id].id)

    def test_create_multiple_instances(self):
        """
         Create multiple instances of different
         classes and save them
        """
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create BaseModel")
            obj_id1 = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create User")
            obj_id2 = output.getvalue().strip()
        self.assertIsNotNone(storage.all()["BaseModel." + obj_id1])
        self.assertIsNotNone(storage.all()["User." + obj_id2])

    def test_print_multiple_instance_ids(self):
        """#Print the ID of each newly created instance"""
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create BaseModel")
            obj_id1 = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create User")
            obj_id2 = output.getvalue().strip()
        self.assertEqual(obj_id1, storage.all()["BaseModel." + obj_id1].id)
        self.assertEqual(obj_id2, storage.all()["User." + obj_id2].id)


if __name__ == '__main__':
    unittest.main()
