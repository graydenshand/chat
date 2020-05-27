#from sqlalchemy import Column, Integer, String
#from sqlalchemy.orm import relationship
from app import db
from marshmallow import Schema, fields
from marshmallow import post_load
from copy import deepcopy

class Messages(fields.Field):
    """
    A field that serializes a Message to it's user_id
    """
    def _serialize(self, messages, attr, obj, **kwargs):
        return [message.id for message in messages]

class UserSchema(Schema):
    id = fields.Integer()
    name = fields.Str(required=True)
    email = fields.Email(required=True)
    links = fields.Method("get_links")

    @post_load
    def make_user(self, data, **kwargs):
        return User(**data)

    def get_links(self, obj):
        return obj.get_links()



class User(db.Model):
    __tablename__ = 'users'
    schema = UserSchema
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    email = db.Column(db.String(120), unique=True)
    messages = db.relationship("Message", back_populates="user")
    links = {
        "messages": '/messages.json?userId={}',
    }

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    def __repr__(self):
        return '<User %r>' % (self.name)

    def get_links(self):
        if self.id:
            links = deepcopy(self.links)
            links['messages'] = links['messages'].format(self.id)
        else:
            links = ''
        return links

    def to_dict(self, sparse=True):
        if sparse == True:
            return {col.name: getattr(self, col.name) for col in self.__table__.columns}
        else:
            return {col.name: getattr(self, col.name) for col in self.__table__.columns if getattr(self, col.name)}
