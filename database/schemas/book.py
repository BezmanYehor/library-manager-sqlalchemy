from pydantic import BaseModel, Field, ConfigDict
from database.schemas import AuthorRead


class BookCreate(BaseModel):
    title: str
    author_id: int
    pages: int = Field(gt=0)


class BookUpdate(BaseModel):
    title: str | None = None
    author_id: int | None = None
    pages: int | None = Field(default=None, gt=0)


class BookRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    title: str
    author: AuthorRead
    pages: int
    is_read: bool
