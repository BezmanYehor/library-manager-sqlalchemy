from database.db import Base, engine, SessionLocal
from database.models import Book
from database.crud import (
    create_book,
    get_books,
    get_book,
    get_book_by_author,
    update_book,
    delete_book,
    search_books,
)
from database.schemas import BookCreate, BookUpdate, BookRead

Base.metadata.create_all(engine)

book_data = BookCreate(
    title="LOL",
    author="Robert Martin",
    pages=464,
)

book_data_update = BookUpdate(
    title="Giga",
    author="Rob Bob",
    pages=1001,
)

# with SessionLocal() as session:
#     book = create_book(session, book_data)


# with SessionLocal() as session:
#     books = get_books(session)
#     for book in books:
#         print(f"{book.id}: {book.title}")


# with SessionLocal() as session:
#     book = get_book(session, 4)
#     if book is None:
#         print("Book not found")
#     else:
#         print(book.title)


# with SessionLocal() as session:
#     books = get_book_by_author(session, "Robert Martin")
#     for book in books:
#         print(f"{book.id}: {book.title}")


# with SessionLocal() as session:
#     book = update_book(session, book_id=1, book_data=book_data_update)
#
#     if book is None:
#         print("Book not found")
#     else:
#         print(f"{book.id}: {book.title}, {book.author}, {book.pages}")


# with SessionLocal() as session:
#     deleted = delete_book(session, 2)
#     if deleted:
#         print("Book delated")
#     else:
#         print("Book not found")

# with SessionLocal() as session:
#     books = search_books(session, author="t", limit=10)
#     for book in books:
#         print(f"{book.id}: {book.title}, {book.author}")


# with SessionLocal() as session:
#     book = session.get(Book, 1)
#     book_data = BookRead.model_validate(book)
#     print(f"{book_data.id}: {book_data.title}")
