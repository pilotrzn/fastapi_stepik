from datetime import datetime
from sqlalchemy import ForeignKey, Integer, String, Text, DateTime
from sqlalchemy.orm import DeclarativeBase, mapped_column, relationship


class Base(DeclarativeBase): ...


class Post(Base):
    __tablename__ = "posts"

    id = mapped_column(Integer, primary_key=True)
    title = mapped_column(String(200), nullable=False)
    content = mapped_column(Text, nullable=False)
    created_at = mapped_column(DateTime, nullable=False, default=datetime.now)

    post = relationship("Comment", back_populates="comments")


class Comment(Base):
    __tablename__ = "comments"

    id = mapped_column(Integer, primary_key=True)
    content = mapped_column(Text, nullable=False)
    created_at = mapped_column(DateTime, nullable=False, default=datetime.now)

    post_id = mapped_column(Integer, ForeignKey("posts.id"), nullable=False)

    comments = relationship("Post", back_populates="post")
