from pydantic import ValidationError

from database.db import SessionLocal
from database.schemas import BookCreate, BookUpdate, IDInput
from app.services import BookService


def print_error(error: Exception) -> None:
    if isinstance(error, ValidationError):
        print("\nValidation error:")

        for err in error.errors():
            location = " -> ".join(str(value) for value in err["loc"])
            print(f"  {location}: {err['msg']}")

    else:
        print(f"\nError: {error}")


def print_book(book) -> None:
    print("\n" + "-" * 40)
    print(f"ID:     {book.id}")
    print(f"Title:  {book.title}")
    print(f"Author: {book.author}")
    print(f"Pages:  {book.pages}")
    print(f"Read:   {'Yes' if book.is_read else 'No'}")
    print("-" * 40)


def create_book() -> None:
    print("\n=== Create book ===")

    try:
        title = input("Title: ")
        author_id = int(input("Author ID: "))
        pages = int(input("Pages: "))

        data = BookCreate(
            title=title,
            author_id=author_id,
            pages=pages,
        )

        with SessionLocal() as session:
            service = BookService(session)
            book = service.create_book(data)

        print("\nBook created successfully!")
        print_book(book)

    except ValidationError as error:
        print_error(error)

    except ValueError as error:
        print_error(error)

    except Exception as error:
        print_error(error)


def update_book() -> None:
    print("\n=== Update book ===")

    try:
        book_id = IDInput(id=int(input("Book ID: ")))

        with SessionLocal() as session:
            service = BookService(session)

            # Check that the book exists before asking for changes
            service.get_book(book_id.id)

            print("\nLeave field empty to keep its current value.")

            title = input("New title: ").strip()
            author_id = input("New author ID: ").strip()
            pages = input("New pages: ").strip()

            update_data = {}

            if title:
                update_data["title"] = title

            if author_id:
                update_data["author_id"] = int(author_id)

            if pages:
                update_data["pages"] = int(pages)

            if not update_data:
                print("\nNo changes were provided.")
                return

            data = BookUpdate(**update_data)

            book = service.update_book(book_id.id, data)

        print("\nBook updated successfully!")
        print_book(book)

    except ValidationError as error:
        print_error(error)

    except ValueError as error:
        print_error(error)

    except Exception as error:
        print_error(error)


def delete_book() -> None:
    print("\n=== Delete book ===")

    try:
        book_id = IDInput(id=int(input("Book ID: ")))

        with SessionLocal() as session:
            service = BookService(session)

            # Check that the book exists before asking for confirmation
            book = service.get_book(book_id.id)

            print_book(book)

            confirmation = (
                input("\nAre you sure you want to delete this book? [y/N]: ")
                .strip()
                .lower()
            )

            if confirmation != "y":
                print("\nDeletion cancelled.")
                return

            service.delete_book(book_id.id)

        print("\nBook deleted successfully!")

    except ValidationError as error:
        print_error(error)

    except ValueError as error:
        print_error(error)

    except Exception as error:
        print_error(error)


def get_book() -> None:
    print("\n=== Get book ===")

    try:
        book_id = IDInput(id=int(input("Book ID: ")))

        with SessionLocal() as session:
            service = BookService(session)
            book = service.get_book(book_id.id)

        print_book(book)

    except ValidationError as error:
        print_error(error)

    except ValueError as error:
        print_error(error)

    except Exception as error:
        print_error(error)


def get_books() -> None:
    print("\n=== All books ===")

    try:
        with SessionLocal() as session:
            service = BookService(session)
            books = service.get_books()

        for book in books:
            print_book(book)

    except ValidationError as error:
        print_error(error)

    except ValueError as error:
        print_error(error)

    except Exception as error:
        print_error(error)


def run_menu() -> None:
    while True:
        print("\n" + "=" * 40)
        print("           BOOK MANAGER")
        print("=" * 40)

        print("1. Create book")
        print("2. Update book")
        print("3. Delete book")
        print("4. Get book")
        print("5. Get all books")
        print("0. Exit")

        choice = input("\nSelect option: ").strip()

        if choice == "1":
            create_book()

        elif choice == "2":
            update_book()

        elif choice == "3":
            delete_book()

        elif choice == "4":
            get_book()

        elif choice == "5":
            get_books()

        elif choice == "0":
            print("\nGoodbye!")
            break

        else:
            print("\nInvalid menu option.")

        input("\nPress Enter to continue...")
