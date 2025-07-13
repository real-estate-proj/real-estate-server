from core.database.base import Base

from sqlalchemy import Column, BigInteger, Text

class Location(Base):
    __tablename__ = "locations"

    id = Column(Text, primary_key=True)
    province = Column(Text)
    ward = Column(Text)
    street = Column(Text)

