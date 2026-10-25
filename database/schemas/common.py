from pydantic import BaseModel, Field


class IDInput(BaseModel):
    id: int = Field(gt=0)
