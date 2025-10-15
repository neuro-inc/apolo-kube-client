from pydantic import BaseModel, Field


class V1KeyToPath(BaseModel):
    key: str | None = Field(None, alias="key")

    mode: int | None = Field(None, alias="mode")

    path: str | None = Field(None, alias="path")
