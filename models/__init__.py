#!/usr/bin/python3
"""
This script initializes a storage system for an application and loads existing
data if available.
"""
from engine.file_storage import FleStorage

storage = FileStorage()
storage.reload()
