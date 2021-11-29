#!/usr/bin/python3
""" State Module for HBNB project """
from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
from models.city import City
import models

# test needed
# add __tablename__ and link to DBStorage
# update state task 6
class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    if getenv('HBNB_MYSQL_DB') == 'db':
        cities = relationship('City', cascade="all", backref="tate")
    else:
        @property
        def cities(self):
            """returns city list instead"""
            res = []
            for i in models.storage.all(City).values():
                if i.state_id == self.id:
                    res.append(i)
            return res
