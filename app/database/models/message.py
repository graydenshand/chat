from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from ..base import Base

class Message(Base):
    __tablename__ = 'messages'
    id = Column(Integer, primary_key=True)
    message = Column(String, nullable=False)
    created_at = Column(Date, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))

    user = relationship("User", back_populates="messages")


    def __init__(self, message=None, created_at=None):
        self.message = message
        self.created_at = created_at

    def __repr__(self):
        return '<Message %r>' % (self.message)