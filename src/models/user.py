from database.base import Base

from sqlalchemy import Column, BigInteger, Text, String, TIMESTAMP, ForeignKey, Boolean, Integer
from sqlalchemy.orm import relationship

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


class EmailVerification(Base):
    __tablename__ = "email_verifications"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(BigInteger, ForeignKey("users.id"), nullable=False, unique=True)
    code = Column(String(6), nullable=False)
    expires_at = Column(TIMESTAMP, nullable=False)
    is_used = Column (Boolean, nullable=False, default=False)

    user = relationship("User", backref="email_verification")
