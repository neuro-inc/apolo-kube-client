from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field


__all__ = ("V1GroupVersionForDiscovery",)


class V1GroupVersionForDiscovery(BaseModel):
    group_version: str | None = Field(
        default=None,
        serialization_alias="groupVersion",
        validation_alias=AliasChoices("group_version", "groupVersion"),
    )

    version: str | None = Field(default=None)
