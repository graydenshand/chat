#from sqlalchemy import Column, Integer, String
#from sqlalchemy.orm import relationship
from app import db
from marshmallow import Schema, fields
from marshmallow import post_load
from copy import deepcopy
import hashlib
from sqlalchemy.orm import validates


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
    password = db.Column(db.String(64))
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

    def is_valid_password(self, password):
        m = hashlib.sha256()
        m.update(bytes(password, 'utf-8'))
        return m.hexdigest() == self.password

    @classmethod
    def hash_password(cls, password):
        m = hashlib.sha256()
        m.update(bytes(password, 'utf-8'))
        return m.hexdigest()

    @validates('password')
    def validate_password(self, key, password):
        # overrides password setter -- converts a string 
        # to a hash before setting the property
        return self.hash_password(password)