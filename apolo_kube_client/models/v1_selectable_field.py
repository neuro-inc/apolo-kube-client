from pydantic import BaseModel, Field


class V1SelectableField(BaseModel):
    json_path: str | None = Field(None, alias="jsonPath")
