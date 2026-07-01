from sqlalchemy import Column, ForeignKey, Table, Integer, String, Text
from sqlalchemy.orm import DeclarativeBase, mapped_column, relationship


class Base(DeclarativeBase): ...


article_tags = Table(
    "article_tags",
    Base.metadata,
    Column("tag_id", Integer, ForeignKey("tags.id"), primary_key=True, index=True),
    Column(
        "article_id", Integer, ForeignKey("articles.id"), primary_key=True, index=True
    ),
)


class Article(Base):
    __tablename__ = "articles"

    id = mapped_column(Integer, primary_key=True)
    title = mapped_column(String(200), nullable=False)
    content = mapped_column(Text, nullable=False)

    tags = relationship("Tag", secondary=article_tags, back_populates="articles")


class Tag(Base):
    __tablename__ = "tags"

    id = mapped_column(Integer, primary_key=True)
    name = mapped_column(String(50), nullable=False, unique=True)

    articles = relationship("Article", secondary=article_tags, back_populates="tags")
