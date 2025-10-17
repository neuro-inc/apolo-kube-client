from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field
from .v1_object_meta import V1ObjectMeta

__all__ = ("V1Secret",)


class V1Secret(BaseModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
    )

    data: dict[str, str] = Field(default={})

    immutable: bool | None = Field(default=None)

    kind: str | None = Field(default=None)

    metadata: V1ObjectMeta

    string_data: dict[str, str] = Field(
        default={},
        serialization_alias="stringData",
        validation_alias=AliasChoices("string_data", "stringData"),
    )

    type: str | None = Field(default=None)
