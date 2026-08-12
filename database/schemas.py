from pydantic import BaseModel, Field, ConfigDict


class BookCreate(BaseModel):
    title: str
    author: str
    pages: int = Field(gt=0)


class BookUpdate(BaseModel):
    title: str | None = None
    author: str | None = None
    pages: int | None = Field(default=None, gt=0)


class BookRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    title: str
    author: str
    pages: int
    is_read: bool
