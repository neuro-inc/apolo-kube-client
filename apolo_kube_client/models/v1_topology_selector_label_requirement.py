from pydantic import BaseModel, Field


class V1TopologySelectorLabelRequirement(BaseModel):
    key: str | None = Field(None, alias="key")

    values: list[str] | None = Field(None, alias="values")
