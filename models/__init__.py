#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage
from os import getenv
# Add a conditional depending of the value of
# the environment variable HBNB_TYPE_STORAGE
# test needed ??
if getenv("HBNB_TYPE_STORAGE") == "db":
    storage = DBStorage()
else:
    storage = FileStorage()

storage.reload()
