from sqlalchemy.orm import Session
from database.models import Book, Author
from database.schemas import AuthorCreate


def create_author(session: Session, author_data: AuthorCreate) -> Author:
    author = Author(name=author_data.name)
    session.add(author)
    session.commit()
    session.refresh(author)
    return author


def get_author(session: Session, author_id: int) -> Author | None:
    return session.get(Author, author_id)


def get_author_books(session: Session, author_id: int) -> list[Book]:
    author = session.get(Author, author_id)
    if author is None:
        raise ValueError("Author not found")

    return author.books
