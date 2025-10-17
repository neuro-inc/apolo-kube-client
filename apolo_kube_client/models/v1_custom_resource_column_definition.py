from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field


__all__ = ("V1CustomResourceColumnDefinition",)


class V1CustomResourceColumnDefinition(BaseModel):
    description: str | None = Field(default=None)

    format: str | None = Field(default=None)

    json_path: str | None = Field(
        default=None,
        serialization_alias="jsonPath",
        validation_alias=AliasChoices("json_path", "jsonPath"),
    )

    name: str | None = Field(default=None)

    priority: int | None = Field(default=None)

    type: str | None = Field(default=None)
