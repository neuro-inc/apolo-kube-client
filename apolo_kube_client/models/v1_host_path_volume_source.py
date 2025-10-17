from __future__ import annotations
from pydantic import BaseModel, Field


__all__ = ("V1HostPathVolumeSource",)


class V1HostPathVolumeSource(BaseModel):
    path: str | None = Field(default=None)

    type: str | None = Field(default=None)
