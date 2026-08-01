from pydantic import BaseModel, Field


class BookCreate(BaseModel):
    title: str
    author: str
    pages: int = Field(gt=0)
