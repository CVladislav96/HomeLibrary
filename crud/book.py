from sqlalchemy import select
from sqlalchemy.exc import IntegrityError

from database.database import new_session
from exceptions.exceptions import BookAlreadyExistsException
from models.book import BooksORM, StatusBook
from schemas.book import *


def add_book_to_db(book: BookCreate) -> BooksORM:
    with new_session() as session:
        book_data = book.model_dump()
        if book_data.get('status') is None:
            book_data['status'] = StatusBook.UNREAD
        book_orm = BooksORM(**book_data)
        session.add(book_orm)
        try:
            session.commit()
            session.refresh(book_orm)
            return book_orm
        except IntegrityError:
            session.rollback()
            raise BookAlreadyExistsException


def get_book_by_id_from_db(book_id: int) -> BooksORM | None:
    with new_session() as session:
        query = select(BooksORM).filter_by(id=book_id)
        result = session.execute(query)
        res: BooksORM | None = result.scalar_one_or_none()
        return res if res else None


def get_all_books_from_db() -> list[BooksORM]:
    with new_session() as session:
        query = select(BooksORM)
        result = session.execute(query)
        return result.scalars().all()


def update_book_in_db(book_id: int, book_data: BookUpdate) -> BooksORM | None:
    with new_session() as session:
        query = select(BooksORM).filter_by(id=book_id)
        result = session.execute(query)
        book: BooksORM | None = result.scalar_one_or_none()

        if book:
            update_data = book_data.model_dump(exclude_unset=True)
            for key, value in update_data.items():
                setattr(book, key, value)

        try:
            session.commit()
            session.refresh(book)
            return book
        except IntegrityError:
            session.rollback()
            raise BookAlreadyExistsException

    return None


def delete_book_from_db(book_id: int) -> None:
    with new_session() as session:
        query = select(BooksORM).filter_by(id=book_id)
        result = session.execute(query)
        book: BooksORM | None = result.scalar_one_or_none()
        if book:
            session.delete(book)
            session.commit()
