from core.database.base import Base

from sqlalchemy import Column, TIMESTAMP, ForeignKey, Text

class Chat(Base):
    __tablename__ = "chats"

    id = Column(Text, primary_key=True)
    user1_id = Column(Text, ForeignKey("users.id"))
    user2_id = Column(Text, ForeignKey("users.id"))
    created_at = Column(TIMESTAMP)


class Message(Base):
    __tablename__ = "messages"

    id = Column(Text, primary_key=True)
    chat_id = Column(Text, ForeignKey("chats.id"))
    sender_id = Column(Text, ForeignKey("users.id"))
    content = Column(Text)
    sent_at = Column(TIMESTAMP)