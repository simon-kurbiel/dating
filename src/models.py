from .database import Base
from sqlalchemy import Column, Integer, String,Boolean,TIMESTAMP, ForeignKey, DECIMAL
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import text


class User(Base):
    __tablename__="users"
    id = Column(Integer, primary_key=True, nullable=False)
    first = Column(String(100), nullable=False)
    last = Column(String(100), nullable=False)
    email = Column(String(100),nullable=False, unique=True)
    password=Column(String(100), nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    
class Images(Base):
    __tablename__ = "images"
    id = Column(Integer, primary_key=True, nullable=False)
    url = Column(String(500), nullable=False)
    user_id= Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    
    owner = relationship("User")
    
    
class Profile(Base):
    __tablename__ = "profile"
    id= Column(Integer, primary_key=True, nullable=False)
    location = Column(String(100), nullable=False)
    longitude = Column(DECIMAL, nullable=False)
    latitude = Column(DECIMAL, nullable=False)
    bio = Column(String(1000), nullable=True)
    college = Column(String(100), nullable=True)
    occupation = Column(String(100), nullable=True)
    looking_for = Column(String(100), nullable=True)
    user_id = Column(Integer,ForeignKey('users.id', ondelete="CASCADE"), nullable=False)
    
    
    
