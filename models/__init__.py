#!/usr/bin/python3
"""
This script initializes a storage system for an application and loads existing
data if available.
"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
