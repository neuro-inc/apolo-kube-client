from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field


__all__ = ("V1EmptyDirVolumeSource",)


class V1EmptyDirVolumeSource(BaseModel):
    medium: str | None = Field(default=None)

    size_limit: str | None = Field(
        default=None,
        serialization_alias="sizeLimit",
        validation_alias=AliasChoices("size_limit", "sizeLimit"),
    )
