#from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
#from sqlalchemy.orm import relationship
from app import db
from marshmallow import Schema, fields
from marshmallow import post_load
from copy import deepcopy

class MessageSchema(Schema):
    id = fields.Integer()
    message = fields.Str(required=True)
    created_at = fields.DateTime(data_key="createdAt")
    user_id = fields.Integer(data_key="userId", required=True)
    channel_id = fields.Integer(data_key="channelId", required=True)
    links = fields.Method('get_links')

    @post_load
    def make_message(self, data, **kwargs):
        return Message(**data)

    def get_links(self, obj):
        return obj.get_links()


class Message(db.Model):
    __tablename__ = 'messages'
    schema = MessageSchema
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    channel_id = db.Column(db.Integer, db.ForeignKey('channels.id'))

    user = db.relationship("User", back_populates="messages")
    channel = db.relationship("Channel", back_populates="messages")

    links = {
        "user": '/user/{}.json',
        "channel": '/channel/{}.json'
    }

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    def __repr__(self):
        return '<Message %r>' % (self.message)

    def get_links(self):
        if self.id:
            links = deepcopy(self.links)
            links['user'] = links['user'].format(self.user_id)
            links['channel'] = links['channel'].format(self.channel_id)
        else:
            links = ''
        return links

    def to_dict(self, sparse=True):
        if sparse == True:
            return {col.name: getattr(self, col.name) for col in self.__table__.columns}
        else:
            return {col.name: getattr(self, col.name) for col in self.__table__.columns if getattr(self, col.name)}