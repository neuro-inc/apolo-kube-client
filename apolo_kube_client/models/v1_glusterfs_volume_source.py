from __future__ import annotations
from pydantic import BaseModel, Field


__all__ = ("V1GlusterfsVolumeSource",)


class V1GlusterfsVolumeSource(BaseModel):
    endpoints: str | None = Field(default_factory=lambda: None)

    path: str | None = Field(default_factory=lambda: None)

    read_only: bool | None = Field(default_factory=lambda: None, alias="readOnly")
