from sqlalchemy.orm import Session
from database.models import Book
from database.schemas import BookCreate, BookUpdate
from sqlalchemy import select
from collections.abc import Sequence


def create_book(session: Session, book_data: BookCreate) -> Book:
    book = Book(title=book_data.title, author=book_data.author, pages=book_data.pages)
    session.add(book)
    session.commit()
    session.refresh(book)
    return book


def get_books(session: Session) -> Sequence[Book]:
    stmt = select(Book)
    books = session.scalars(stmt).all()
    return books


def get_book(session: Session, book_id: int) -> Book | None:
    return session.get(Book, book_id)


def get_book_by_author(session: Session, author: str) -> Sequence[Book]:
    stmt = select(Book).where(Book.author == author)
    return session.scalars(stmt).all()


def search_books(
    session: Session,
    search: str | None = None,
    author: str | None = None,
    min_pages: int | None = None,
    limit: int = 1,
) -> Sequence[Book]:

    stmt = select(Book)

    if search is not None:
        stmt = stmt.where(Book.title.contains(search))

    if author is not None:
        stmt = stmt.where(Book.author.contains(author))

    if min_pages is not None:
        stmt = stmt.where(Book.pages >= min_pages)

    stmt = stmt.order_by(Book.title).limit(limit)

    return session.scalars(stmt).all()


def update_book(session: Session, book_id: int, book_data: BookUpdate) -> Book | None:
    book = session.get(Book, book_id)
    if book is None:
        return None

    update_data = book_data.model_dump(exclude_unset=True)

    for field, value in update_data.items():
        setattr(book, field, value)

    session.commit()
    session.refresh(book)

    return book


def delete_book(session: Session, book_id: int) -> bool:
    book = session.get(Book, book_id)

    if book is None:
        return False

    session.delete(book)
    session.commit()

    return True
