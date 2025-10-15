from pydantic import BaseModel, Field


class V1Capabilities(BaseModel):
    add: list[str] | None = Field(None, alias="add")

    drop: list[str] | None = Field(None, alias="drop")
