from __future__ import annotations

from pydantic import BaseModel, Field

__all__ = ("V1CustomResourceColumnDefinition",)


class V1CustomResourceColumnDefinition(BaseModel):
    description: str | None = Field(None, alias="description")

    format: str | None = Field(None, alias="format")

    json_path: str | None = Field(None, alias="jsonPath")

    name: str | None = Field(None, alias="name")

    priority: int | None = Field(None, alias="priority")

    type: str | None = Field(None, alias="type")
