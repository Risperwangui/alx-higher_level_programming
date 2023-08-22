#!/usr/bin/python3
"""this contains the class definition of a state and instance base"""

import sqlalchemy
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    """This is a representation of a state"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=TRUE)
    name = Column(String(128), nullable=False)
