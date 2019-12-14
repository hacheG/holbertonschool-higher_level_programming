#!/usr/bin/python3
# bla-bla-bla

import sqlalchemy
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """return to classes"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128))
