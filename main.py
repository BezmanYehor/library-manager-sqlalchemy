from database.db import Base, engine, SessionLocal
import database.models
from database.crud import create_book, get_books, get_book, get_book_by_author
from database.schemas import BookCreate

Base.metadata.create_all(engine)

book_data = BookCreate(
    title="LOL",
    author="Robert Martin",
    pages=464,
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


with SessionLocal() as session:
    books = get_book_by_author(session, "Robert Martin")
    for book in books:
        print(f"{book.id}: {book.title}")
