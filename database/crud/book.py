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
    author = session.get(Author, book_data.author_id)

    if author is None:
        raise ValueError("Author not found")

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


def search_books(
    session: Session,
    search: str | None = None,
    author_name: str | None = None,
    min_pages: int | None = None,
    limit: int = 1,
) -> Sequence[Book]:

    stmt = select(Book)

    if search is not None:
        stmt = stmt.where(Book.title.contains(search))

    if author_name is not None:
        stmt = (
            select(Book)
            .join(Book.author)
            .where(Author.name == author_name)
            .options(selectinload(Book.author))
        )

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
