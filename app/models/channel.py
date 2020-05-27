#from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
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

class ChannelSchema(Schema):
    id = fields.Integer()
    name = fields.Str(required=True)
    created_at = fields.DateTime(data_key="createdAt")
    links = fields.Method("get_links")

    @post_load
    def make_channel(self, data, **kwargs):
        return Channel(**data)

    def get_links(self, obj):
        return obj.get_links()


class Channel(db.Model):
    __tablename__ = 'channels'
    schema = ChannelSchema
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)

    messages = db.relationship("Message", back_populates="channel")

    links = {
        "messages": '/messages.json?channelId={}',
    }

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    def __repr__(self):
        return '<Channel %r>' % (self.name)

    def get_links(self):
        if self.id:
            links = deepcopy(self.links)
            links['messages'] = links['messages'].format(self.id)
        else:
            links = ''
        return links