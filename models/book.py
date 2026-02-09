from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase
from enum import Enum

class Base(DeclarativeBase):
    pass

class StatusBook(Enum):
    READ = "read"
    UNREAD = "unread"

class BooksORM(Base):
    __tablename__ = 'books'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String(100))
    author: Mapped[str] = mapped_column(String(100))
    description: Mapped[str | None] = mapped_column(String(300))
    published_year: Mapped[int]
    status: Mapped[StatusBook]






