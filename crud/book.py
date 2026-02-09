from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from database import new_session
from exceptions.exceptions import BookAlreadyExistsException
from models.book import BooksORM

def add_book_to_db(
        title: str,
        author: str,
        description: str | None = None,
        published_year: int | None = None
)-> None:
    with new_session() as session:
        book = BooksORM(title=title, author=author, description=description, published_year=published_year)
        session.add(book)
        try:
            session.commit()
        except IntegrityError:
            raise BookAlreadyExistsException

def get_book_by_id_from_db(book_id: int) -> BooksORM | None:
    with new_session() as session:
        query = select(BooksORM).filter_by(id=book_id)
        result = session.execute(query)
        res: BooksORM | None = result.scalar_one_or_none()
        return res.BooksORM if res else None

def get_all_books_from_db() -> list[BooksORM]:
    with new_session() as session:
        query = select(BooksORM)
        result = session.execute(query)
        return result.scalars().all()

def update_book_in_db(
        book_id: int,
        title: str,
        author: str,
        description: str | None = None,
        published_year: int | None = None,
) -> None:
    with new_session() as session:
        query = select(BooksORM).filter_by(id=book_id)
        result = session.execute(query)
        book: BooksORM | None = result.scalar_one_or_none()
        if book:
            book.title = title
            book.author = author
            book.description = description
            book.published_year = published_year
            session.commit()

def delete_book_from_db(book_id: int) -> None:
    with new_session() as session:
        query = select(BooksORM).filter_by(id=book_id)
        result = session.execute(query)
        book: BooksORM | None = result.scalar_one_or_none()
        if book:
            session.delete(book)
            session.commit()



