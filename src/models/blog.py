from database.base import Base

from sqlalchemy import Column, BigInteger, Text, TIMESTAMP, ForeignKey, CheckConstraint

class Blog(Base):
    __tablename__ = "blogs"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    user_id = Column(BigInteger, ForeignKey("users.id"))
    title = Column(Text)
    content = Column(Text)
    created_at = Column(TIMESTAMP)

class Comment(Base):
    __tablename__ = "comments"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    blog_id = Column(BigInteger, ForeignKey("blogs.id"))
    user_id = Column(BigInteger, ForeignKey("users.id"))
    content = Column(Text)
    created_at = Column(TIMESTAMP)

class Vote(Base):
    __tablename__ = "votes"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    user_id = Column(BigInteger, ForeignKey("users.id"))
    blog_id = Column(BigInteger, ForeignKey("blogs.id"))
    vote_type = Column(Text)
    created_at = Column(TIMESTAMP)

    __table_args__ = (
        CheckConstraint("vote_type IN ('upvote', 'downvote')", name="check_vote_type"),
    )


class BlogReport(Base):
    __tablename__ = "blog_reports"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    blog_id = Column(BigInteger, ForeignKey("blogs.id"))
    reporter_id = Column(BigInteger, ForeignKey("users.id"))
    reason = Column(Text)
    created_at = Column(TIMESTAMP)

class CommentReport(Base):
    __tablename__ = "comment_reports"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    comment_id = Column(BigInteger, ForeignKey("comments.id"))
    reporter_id = Column(BigInteger, ForeignKey("users.id"))
    reason = Column(Text)
    created_at = Column(TIMESTAMP)
