from sqlalchemy.orm import Session
from database.schemas import BookCreate, BookRead, BookUpdate
from database.crud import (
    get_author,
    create_book,
    get_book,
    get_books,
    update_book,
    delete_book,
)


class BookService:
    def __init__(self, session: Session):
        self.session = session

    def create_book(self, data: BookCreate) -> BookRead:
        author = get_author(self.session, data.author_id)
        if author is None:
            raise ValueError("Author does not exist")

        book = create_book(self.session, data)
        return BookRead.model_validate(book)

    def update_book(self, book_id: int, data: BookUpdate) -> BookRead:
        book = get_book(self.session, book_id)
        if book is None:
            raise ValueError("Book not found")

        if data.author_id is not None:
            author = get_author(self.session, data.author_id)
            if author is None:
                raise ValueError("Author does not exist")

        updated_book = update_book(self.session, book, data)
        return BookRead.model_validate(updated_book)

    def delete_book(self, book_id: int) -> None:
        book = get_book(self.session, book_id)
        if book is None:
            raise ValueError("Book not found")
        delete_book(self.session, book)

    def get_book(self, book_id: int) -> BookRead:
        book = get_book(self.session, book_id)

        if book is None:
            raise ValueError("Book not found")

        return BookRead.model_validate(book)

    def get_books(self) -> list[BookRead]:
        books = get_books(self.session)
        if not books:
            raise ValueError("No books found")

        return [BookRead.model_validate(book) for book in books]
