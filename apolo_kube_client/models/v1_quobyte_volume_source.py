from __future__ import annotations
from pydantic import BaseModel, Field


__all__ = ("V1QuobyteVolumeSource",)


class V1QuobyteVolumeSource(BaseModel):
    group: str | None = Field(default_factory=lambda: None, alias="group")

    read_only: bool | None = Field(default_factory=lambda: None, alias="readOnly")

    registry: str | None = Field(default_factory=lambda: None, alias="registry")

    tenant: str | None = Field(default_factory=lambda: None, alias="tenant")

    user: str | None = Field(default_factory=lambda: None, alias="user")

    volume: str | None = Field(default_factory=lambda: None, alias="volume")
