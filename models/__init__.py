#!/usr/bin/python3
"""__initializes directory as a package."""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
