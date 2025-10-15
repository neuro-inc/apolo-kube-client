from pydantic import BaseModel, Field


class V1NonResourceAttributes(BaseModel):
    path: str | None = Field(None, alias="path")

    verb: str | None = Field(None, alias="verb")
