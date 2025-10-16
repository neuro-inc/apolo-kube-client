from __future__ import annotations

from pydantic import BaseModel, Field

__all__ = ("V1CustomResourceDefinitionNames",)


class V1CustomResourceDefinitionNames(BaseModel):
    categories: list[str] | None = Field(None, alias="categories")

    kind: str | None = Field(None, alias="kind")

    list_kind: str | None = Field(None, alias="listKind")

    plural: str | None = Field(None, alias="plural")

    short_names: list[str] | None = Field(None, alias="shortNames")

    singular: str | None = Field(None, alias="singular")
