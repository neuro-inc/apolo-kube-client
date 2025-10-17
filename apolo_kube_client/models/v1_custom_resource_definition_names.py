from __future__ import annotations
from pydantic import BaseModel, Field


__all__ = ("V1CustomResourceDefinitionNames",)


class V1CustomResourceDefinitionNames(BaseModel):
    categories: list[str] = Field(default_factory=lambda: [])

    kind: str | None = Field(default_factory=lambda: None)

    list_kind: str | None = Field(default_factory=lambda: None, alias="listKind")

    plural: str | None = Field(default_factory=lambda: None)

    short_names: list[str] = Field(default_factory=lambda: [], alias="shortNames")

    singular: str | None = Field(default_factory=lambda: None)
