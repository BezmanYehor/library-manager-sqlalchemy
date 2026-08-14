from pydantic import BaseModel, Field, ConfigDict


class AuthorCreate(BaseModel):
    name: str = Field(min_length=3, max_length=100)


class AuthorRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str
