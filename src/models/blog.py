from core.database.base import Base

from sqlalchemy import Column, Text, TIMESTAMP, ForeignKey, CheckConstraint

class Blog(Base):
    __tablename__ = "blogs"

    id = Column(Text, primary_key=True)
    user_id = Column(Text, ForeignKey("users.id"))
    title = Column(Text)
    content = Column(Text)
    created_at = Column(TIMESTAMP)

class Comment(Base):
    __tablename__ = "comments"

    id = Column(Text, primary_key=True)
    blog_id = Column(Text, ForeignKey("blogs.id"))
    user_id = Column(Text, ForeignKey("users.id"))
    content = Column(Text)
    created_at = Column(TIMESTAMP)

class Vote(Base):
    __tablename__ = "votes"

    id = Column(Text, primary_key=True)
    user_id = Column(Text, ForeignKey("users.id"))
    blog_id = Column(Text, ForeignKey("blogs.id"))
    vote_type = Column(Text)
    created_at = Column(TIMESTAMP)

    __table_args__ = (
        CheckConstraint("vote_type IN ('upvote', 'downvote')", name="check_vote_type"),
    )


class BlogReport(Base):
    __tablename__ = "blog_reports"

    id = Column(Text, primary_key=True)
    blog_id = Column(Text, ForeignKey("blogs.id"))
    reporter_id = Column(Text, ForeignKey("users.id"))
    reason = Column(Text)
    created_at = Column(TIMESTAMP)

class CommentReport(Base):
    __tablename__ = "comment_reports"

    id = Column(Text, primary_key=True)
    comment_id = Column(Text, ForeignKey("comments.id"))
    reporter_id = Column(Text, ForeignKey("users.id"))
    reason = Column(Text)
    created_at = Column(TIMESTAMP)
