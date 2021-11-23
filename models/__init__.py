#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from .amenity import Amenity
from .base_model import BaseModel
from .city import City
from .place import Place
from .review import Review
from .state import State
from .user import User
import os
from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage
# Add a conditional depending of the value of
# the environment variable HBNB_TYPE_STORAGE
# test needed ??
if os.getenv("HBNB_TYPE_STORAGE") == "db":
    storage = DBStorage()
else:
    storage = FileStorage()
storage.reload()
