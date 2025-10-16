from __future__ import annotations

from pydantic import BaseModel, Field

__all__ = ("V1QuobyteVolumeSource",)


class V1QuobyteVolumeSource(BaseModel):
    group: str | None = Field(None, alias="group")

    read_only: bool | None = Field(None, alias="readOnly")

    registry: str | None = Field(None, alias="registry")

    tenant: str | None = Field(None, alias="tenant")

    user: str | None = Field(None, alias="user")

    volume: str | None = Field(None, alias="volume")
