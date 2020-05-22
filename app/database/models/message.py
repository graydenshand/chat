from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app import db
from marshmallow import Schema, fields
from marshmallow import post_load

class MessageSchema(Schema):
    id = fields.Integer()
    message = fields.Str(required=True)
    created_at = fields.DateTime(data_key="createdAt")
    user_id = fields.Integer(data_key="userId", required=True)

    @post_load
    def make_message(self, data, **kwargs):
        return Message(**data)


class Message(db.Base):
    __tablename__ = 'messages'
    schema = MessageSchema
    id = Column(Integer, primary_key=True)
    message = Column(String, nullable=False)
    created_at = Column(DateTime, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))

    user = relationship("User", back_populates="messages")


    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    def __repr__(self):
        return '<Message %r>' % (self.message)