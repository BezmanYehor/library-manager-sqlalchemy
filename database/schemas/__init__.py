from database.schemas.author import AuthorRead, AuthorCreate
from database.schemas.book import BookCreate, BookRead, BookUpdate
from database.schemas.common import IDInput

__all__ = [
    "IDInput",
    "AuthorRead",
    "AuthorCreate",
    "BookUpdate",
    "BookRead",
    "BookCreate",
]
