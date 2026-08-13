from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database.db import Base


class Book(Base):
    __tablename__ = "books"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    author_id: Mapped[int] = mapped_column(ForeignKey("authors.id"))
    pages: Mapped[int]
    is_read: Mapped[bool] = mapped_column(default=False)
    author: Mapped["Author"] = relationship(back_populates="books")
