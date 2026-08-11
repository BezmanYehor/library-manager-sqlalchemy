from sqlalchemy.orm import Session
from database.models import Book
from database.schemas import BookCreate
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
