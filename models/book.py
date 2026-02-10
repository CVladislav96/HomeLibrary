from sqlalchemy import Integer, String, Enum as SQLEnum
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase
from enum import Enum
from models import Base



class StatusBook(str,Enum):
    READ = "read"
    READING = "reading"
    UNREAD = "unread"

class BooksORM(Base):
    __tablename__ = 'books'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String(100))
    author: Mapped[str] = mapped_column(String(100))
    description: Mapped[str | None] = mapped_column(String(300))
    published_year: Mapped[int | None] = mapped_column(Integer)
    status: Mapped[StatusBook] = mapped_column(
        SQLEnum(StatusBook),
        default=StatusBook.UNREAD,
        nullable=False
    )






