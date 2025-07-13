from core.database.base import Base

from sqlalchemy import Column, Text,  Numeric, Integer, Boolean, TIMESTAMP, ForeignKey, CheckConstraint

class PropertyType(Base):
    __tablename__ = "property_types"

    id = Column(Text, primary_key=True)
    name = Column(Text)


class Property(Base):
    __tablename__ = "properties"

    id = Column(Text, primary_key=True)
    user_id = Column(Text, ForeignKey("users.id"))
    type_id = Column(Text, ForeignKey("property_types.id"))
    location_id = Column(Text, ForeignKey("locations.id"))
    title = Column(Text)
    description = Column(Text)
    price = Column(Numeric)
    area = Column(Numeric)
    bedrooms = Column(Integer)
    bathrooms = Column(Integer)
    status = Column(Text)
    featured = Column(Boolean)
    published_at = Column(TIMESTAMP)
    is_verified = Column(Boolean)

    __table_args__ = (
        CheckConstraint(status.in_(["available", "sold", "rented"]), name="check_property_status"),
    )


class Image(Base):
    __tablename__ = "images"

    id = Column(Text, primary_key=True)
    property_id = Column(Text, ForeignKey("properties.id"))
    url = Column(Text)

class Tag(Base):
    __tablename__ = "tags"

    id = Column(Text, primary_key=True)
    name = Column(Text)

class PropertyTag(Base):
    __tablename__ = "property_tags"

    property_id = Column(Text, ForeignKey("properties.id"), primary_key=True)
    tag_id = Column(Text, ForeignKey("tags.id"), primary_key=True)


class Report(Base):
    __tablename__ = "reports"

    id = Column(Text, primary_key=True)
    property_id = Column(Text, ForeignKey("properties.id"))
    reporter_id = Column(Text, ForeignKey("users.id"))
    reason = Column(Text)
    created_at = Column(TIMESTAMP)