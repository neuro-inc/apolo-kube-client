from __future__ import annotations
from pydantic import BaseModel, Field


__all__ = ("V1CustomResourceColumnDefinition",)


class V1CustomResourceColumnDefinition(BaseModel):
    description: str | None = Field(default_factory=lambda: None)

    format: str | None = Field(default_factory=lambda: None)

    json_path: str | None = Field(default_factory=lambda: None, alias="jsonPath")

    name: str | None = Field(default_factory=lambda: None)

    priority: int | None = Field(default_factory=lambda: None)

    type: str | None = Field(default_factory=lambda: None)
