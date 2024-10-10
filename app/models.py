from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)

    designs = relationship("Design", back_populates="user")

class Design(Base):
    __tablename__ = 'designs'
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    name = Column(String, index=True)
    style = Column(String)
    layout = Column(String)

    user = relationship("User", back_populates="designs")
    objects = relationship("Object", back_populates="design")

class Object(Base):
    __tablename__ = 'objects'
    id = Column(Integer, primary_key=True, index=True)
    design_id = Column(Integer, ForeignKey('designs.id'))
    name = Column(String)
    type = Column(String)

    design = relationship("Design", back_populates="objects")
