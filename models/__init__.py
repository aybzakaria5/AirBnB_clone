#!/usr/bin/python3
"""
This script initializes a storage system for an application and loads existing
data if available.
"""
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

storage = FileStorage()
storage.reload()
