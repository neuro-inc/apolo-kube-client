from __future__ import annotations
from pydantic import BaseModel, Field


__all__ = ("V1QuobyteVolumeSource",)


class V1QuobyteVolumeSource(BaseModel):
    group: str | None = Field(default_factory=lambda: None)

    read_only: bool | None = Field(default_factory=lambda: None, alias="readOnly")

    registry: str | None = Field(default_factory=lambda: None)

    tenant: str | None = Field(default_factory=lambda: None)

    user: str | None = Field(default_factory=lambda: None)

    volume: str | None = Field(default_factory=lambda: None)
