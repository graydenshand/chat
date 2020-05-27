#from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
#from sqlalchemy.orm import relationship
from app import db
from marshmallow import Schema, fields
from marshmallow import post_load

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
    messages = Messages()

    @post_load
    def make_channel(self, data, **kwargs):
        return Channel(**data)


class Channel(db.Model):
    __tablename__ = 'channels'
    schema = ChannelSchema
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)

    messages = db.relationship("Message", back_populates="channel")

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    def __repr__(self):
        return '<Channel %r>' % (self.name)