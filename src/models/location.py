from core.database.base import Base

from sqlalchemy import Column, BigInteger, Text

class Location(Base):
    __tablename__ = "locations"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    province = Column(Text)
    ward = Column(Text)
    street = Column(Text)

