from core.database.base import Base

from sqlalchemy import Column, BigInteger, Text, TIMESTAMP, ForeignKey, Boolean

class User(Base):
    __tablename__ = "users"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    name = Column(Text)
    email = Column(Text, unique=True)
    phone = Column(Text)
    password_hash = Column(Text)
    role = Column(Text, nullable=False)
    avatar_url = Column(Text)
    created_at = Column(TIMESTAMP)
    is_verified = Column (Boolean)

class Admin(Base):
    __tablename__ = "admins"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    user_id = Column(BigInteger, ForeignKey("users.id"))
    is_super = Column(Boolean)


class Favorite(Base):
    __tablename__ = "favorites"

    user_id = Column(BigInteger, ForeignKey("users.id"), primary_key=True)
    property_id = Column(BigInteger, ForeignKey("properties.id"), primary_key=True)

