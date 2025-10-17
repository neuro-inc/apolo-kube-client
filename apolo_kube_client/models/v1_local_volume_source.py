from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field


__all__ = ("V1LocalVolumeSource",)


class V1LocalVolumeSource(BaseModel):
    fs_type: str | None = Field(
        default=None,
        serialization_alias="fsType",
        validation_alias=AliasChoices("fs_type", "fsType"),
    )

    path: str | None = Field(default=None)
