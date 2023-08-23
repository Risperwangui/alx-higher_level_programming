#!/usr/bin/python3
"""
this contains the cities
"""

import sqlalchemy
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base, State


class City(Base):
    """this represents the cities"""
    __tablename__ = "cities"
    id = Column(Interger, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'))
