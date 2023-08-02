#!/usr/bin/python3
"""
    The class definition of a State and an instance Base = declarative_base():
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
import sys


Base = declarative_base()


# The above class represents a State entity with an id and name attribute.
class State(Base):

    """ The code block you provided is defining a SQLAlchemy model
        class called `State`.
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
