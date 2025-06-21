from core.database.base import Base

from sqlalchemy import Column, BigInteger, TIMESTAMP, ForeignKey, Text

class Chat(Base):
    __tablename__ = "chats"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    user1_id = Column(BigInteger, ForeignKey("users.id"))
    user2_id = Column(BigInteger, ForeignKey("users.id"))
    created_at = Column(TIMESTAMP)


class Message(Base):
    __tablename__ = "messages"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    chat_id = Column(BigInteger, ForeignKey("chats.id"))
    sender_id = Column(BigInteger, ForeignKey("users.id"))
    content = Column(Text)
    sent_at = Column(TIMESTAMP)