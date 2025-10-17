from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field


__all__ = ("V1FileKeySelector",)


class V1FileKeySelector(BaseModel):
    key: str | None = Field(default=None)

    optional: bool | None = Field(default=None)

    path: str | None = Field(default=None)

    volume_name: str | None = Field(
        default=None,
        serialization_alias="volumeName",
        validation_alias=AliasChoices("volume_name", "volumeName"),
    )
