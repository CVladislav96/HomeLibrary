from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


from .book import BooksORM
from .user import User
