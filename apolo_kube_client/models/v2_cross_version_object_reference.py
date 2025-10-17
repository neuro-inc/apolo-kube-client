from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field


__all__ = ("V2CrossVersionObjectReference",)


class V2CrossVersionObjectReference(BaseModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
    )

    kind: str | None = Field(default=None)

    name: str | None = Field(default=None)
