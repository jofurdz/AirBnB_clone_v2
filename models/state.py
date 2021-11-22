#!/usr/bin/python3
""" State Module for HBNB project """
from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
from models.city import City
import models

from models.city import City
# test needed
# add __tablename__ and link to DBStorage
# update state task 6
class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'

    if getenv('HBNB_MYSQL_DB') == 'db':
        name = Column(String(128),nullable=False)
        cities = relationship(City, cascade="all", backref="States")

    name = ""

    @property
    def cities(self):
        """returns city list instead"""
        res = []
        for i in models.storage.all(City).values():
            if i.state_id == self.id:
                res.append(i)
        return res
