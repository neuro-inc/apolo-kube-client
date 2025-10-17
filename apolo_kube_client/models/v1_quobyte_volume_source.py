from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field


__all__ = ("V1QuobyteVolumeSource",)


class V1QuobyteVolumeSource(BaseModel):
    group: str | None = Field(default=None)

    read_only: bool | None = Field(
        default=None,
        serialization_alias="readOnly",
        validation_alias=AliasChoices("read_only", "readOnly"),
    )

    registry: str | None = Field(default=None)

    tenant: str | None = Field(default=None)

    user: str | None = Field(default=None)

    volume: str | None = Field(default=None)
