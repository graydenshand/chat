from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app import db
from marshmallow import Schema, fields
from marshmallow import post_load

class UserSchema(Schema):
    id = fields.Integer()
    name = fields.Str(required=True)
    email = fields.Email(required=True)

    @post_load
    def make_user(self, data, **kwargs):
        return User(**data)


class User(db.Base):
    __tablename__ = 'users'
    schema = UserSchema
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    email = Column(String(120), unique=True)

    messages = relationship("Message", back_populates="user")

    def __init__(self, name=None, email=None):
        self.name = name
        self.email = email

    def __repr__(self):
        return '<User %r>' % (self.name)