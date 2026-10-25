from sqlalchemy.orm import Session, selectinload
from database.models import Book, Author
from database.schemas import BookCreate, BookUpdate
from sqlalchemy import select
from collections.abc import Sequence


def get_books_with_authors(session: Session) -> list[Book]:
    stmt = select(Book).options(selectinload(Book.author))
    return list(session.scalars(stmt).all())


def get_book_by_author(session: Session, author_name: str) -> list[Book]:
    stmt = (
        select(Book)
        .join(Book.author)
        .where(Author.name == author_name)
        .options(selectinload(Book.author))
    )
    return list(session.scalars(stmt).all())


def create_book(session: Session, book_data: BookCreate) -> Book:
    book = Book(
        title=book_data.title, author_id=book_data.author_id, pages=book_data.pages
    )

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


def update_book(session: Session, book: Book, book_data: BookUpdate) -> Book:
    update_data = book_data.model_dump(exclude_unset=True)

    for field, value in update_data.items():
        setattr(book, field, value)

    session.commit()
    session.refresh(book)

    return book


def delete_book(session: Session, book: Book) -> None:
    session.delete(book)
    session.commit()
