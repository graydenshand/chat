from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from ..base import Base, SerializerMixin

class User(Base, SerializerMixin):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    email = Column(String(120), unique=True)

    messages = relationship("Message", back_populates="user")

    def __init__(self, name=None, email=None):
        self.name = name
        self.email = email

    def __repr__(self):
        return '<User %r>' % (self.name)