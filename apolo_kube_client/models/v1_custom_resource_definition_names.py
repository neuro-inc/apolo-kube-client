from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field


__all__ = ("V1CustomResourceDefinitionNames",)


class V1CustomResourceDefinitionNames(BaseModel):
    categories: list[str] = Field(default=[])

    kind: str | None = Field(default=None)

    list_kind: str | None = Field(
        default=None,
        serialization_alias="listKind",
        validation_alias=AliasChoices("list_kind", "listKind"),
    )

    plural: str | None = Field(default=None)

    short_names: list[str] = Field(
        default=[],
        serialization_alias="shortNames",
        validation_alias=AliasChoices("short_names", "shortNames"),
    )

    singular: str | None = Field(default=None)
