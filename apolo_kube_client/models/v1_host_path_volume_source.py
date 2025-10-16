from __future__ import annotations

from pydantic import BaseModel, Field

__all__ = ("V1HostPathVolumeSource",)


class V1HostPathVolumeSource(BaseModel):
    path: str | None = Field(None, alias="path")

    type: str | None = Field(None, alias="type")
