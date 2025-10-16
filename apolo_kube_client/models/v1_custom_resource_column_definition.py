from __future__ import annotations
from pydantic import BaseModel, Field


__all__ = ("V1CustomResourceColumnDefinition",)


class V1CustomResourceColumnDefinition(BaseModel):
    description: str | None = Field(default_factory=lambda: None, alias="description")

    format: str | None = Field(default_factory=lambda: None, alias="format")

    json_path: str | None = Field(default_factory=lambda: None, alias="jsonPath")

    name: str | None = Field(default_factory=lambda: None, alias="name")

    priority: int | None = Field(default_factory=lambda: None, alias="priority")

    type: str | None = Field(default_factory=lambda: None, alias="type")
