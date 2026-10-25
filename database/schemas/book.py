from pydantic import BaseModel, Field, ConfigDict
from database.schemas import AuthorRead


class BookCreate(BaseModel):
    title: str = Field(min_length=1, max_length=100)
    author_id: int = Field(gt=0)
    pages: int = Field(gt=0)


class BookUpdate(BaseModel):
    title: str | None = Field(default=None, min_length=1, max_length=100)
    author_id: int | None = Field(default=None, gt=0)
    pages: int | None = Field(default=None, gt=0)


class BookRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    title: str
    author: AuthorRead
    pages: int
    is_read: bool
