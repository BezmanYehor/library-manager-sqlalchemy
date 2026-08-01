from sqlalchemy.orm import Mapped, mapped_column
from database.db import Base


class Book(Base):
    __tablename__ = "books"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    author: Mapped[str]
    pages: Mapped[int]
    is_read: Mapped[bool] = mapped_column(default=False)
