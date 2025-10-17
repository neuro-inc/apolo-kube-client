from __future__ import annotations
from pydantic import BaseModel, Field


__all__ = ("V1EmptyDirVolumeSource",)


class V1EmptyDirVolumeSource(BaseModel):
    medium: str | None = Field(default_factory=lambda: None)

    size_limit: str | None = Field(default_factory=lambda: None, alias="sizeLimit")
