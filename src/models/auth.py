from core.database.base import Base

from sqlalchemy import Column, Text, String, TIMESTAMP, ForeignKey, Boolean, Integer, BigInteger
from sqlalchemy.orm import relationship


class EmailVerification(Base):
    __tablename__ = "email_verifications"

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(Text, ForeignKey("users.email"), unique=True)
    code = Column(String(6), nullable=False)
    expires_at = Column(TIMESTAMP, nullable=False)
    is_used = Column (Boolean, nullable=False, default=False)

    user = relationship("User", backref="email_verification")


class RevokedToken (Base):
    __tablename__ = "revoked_token"

    access_token = Column (Text, unique=True, nullable=False, primary_key=True)
    refresh_token = Column (Text, unique=True, nullable=False, primary_key=True)


class BlackList (Base):
    __tablename__ = "black_list"
    
    id = Column (BigInteger, primary_key=True, autoincrement=True)
    email = Column (Text, ForeignKey ("users.email"), unique=True)
    attempts = Column (Integer)