#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, ForeignKey
import os

class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    # test needed
    # add __tablename__ and link to DBStorage
    __tablename__ = 'cities'
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    name = Column(String(128), nullable=False)
