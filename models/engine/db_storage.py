#!/usr/bin/python3
"""This module defines a class to manage DataBase storage for hbnb clone"""
import json
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.expression import delete
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from os import getenv
from sqlalchemy import create_engine


# SQL engine test will be needed
# New engine DBStorage: (models/engine/db_storage.py)

class  DBStorage:
    """ SQL DB Storage"""
# Private class attributes
    __engine: None
    __session: None

    def __init__(self):
        # create the engine
        # linked to the MySQL database and user created before
        # (hbnb_dev and hbnb_dev_db):
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}/{}'.format(
                getenv("HBNB_MYSQL_USER"),
                getenv("HBNB_MYSQL_PWD"),
                getenv("HBNB_MYSQL_HOST@localhost"),
                getenv("HBNB_MYSQL_DB"),
                pool_pre_ping=True))
        Base.metadata.create_all(self.__engine)
        if getenv("HBNB_ENV") == "tests":
            Base.matadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """
        Returns all instances of a class if the class name is passed.
        If it's empty, return all instances of valid classes.
        """
        # Sub-classes = ['Plases', 'States', 'Review', 'City', 'User', 'Amenity]
        all_dict = {}
        if cls:
            result = self.__session.query(eval(cls)).all()
            for item in result:
                key = '{}.{}'.format(item.__class__.name__, item.id)
                all_dict[key] = item
        else:
            for x in Base.__subclasses__():
                result = self.__session.query(x).all()
                for item in result:
                      key = '{}.{}'.format(item.__class__.__name__, item.id)
                all_dict[key] = item
        return all_dict

    def new(self, obj):
        """NEW"""
        try:
            self.__session.add(obj)
        except:
            pass

    def save(self):
        """Save"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        Base.metadata.create_all(self.__engine)
        curr = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(curr)


