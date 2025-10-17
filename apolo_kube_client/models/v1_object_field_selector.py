from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field


__all__ = ("V1ObjectFieldSelector",)


class V1ObjectFieldSelector(BaseModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
    )

    field_path: str | None = Field(
        default=None,
        serialization_alias="fieldPath",
        validation_alias=AliasChoices("field_path", "fieldPath"),
    )
