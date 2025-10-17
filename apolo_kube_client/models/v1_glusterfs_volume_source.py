from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field


__all__ = ("V1GlusterfsVolumeSource",)


class V1GlusterfsVolumeSource(BaseModel):
    endpoints: str | None = Field(default=None)

    path: str | None = Field(default=None)

    read_only: bool | None = Field(
        default=None,
        serialization_alias="readOnly",
        validation_alias=AliasChoices("read_only", "readOnly"),
    )
