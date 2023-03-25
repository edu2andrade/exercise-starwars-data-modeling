import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    user_id = Column(Integer, primary_key=True)
    user_name = Column(String(120), nullable=False)
    email = Column(String(120), nullable=False)
    password = Column(String(250), nullable=False)

class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name=Column(String(120), nullable=False)
    population=Column(Integer, nullable=False)

class Characters(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    height = Column(Integer)
    mass = Column(Integer)
    gender = Column(String(12))
    name = Column(String(120))

class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    planet_id = Column(Integer, ForeignKey('planets.id'))
    planet = relationship(Planets)
    character_id = Column(Integer, ForeignKey('characters.id'))
    characters = relationship(Characters)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
