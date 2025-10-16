from __future__ import annotations

from pydantic import BaseModel, Field

__all__ = ("V1EmptyDirVolumeSource",)


class V1EmptyDirVolumeSource(BaseModel):
    medium: str | None = Field(None, alias="medium")

    size_limit: str | None = Field(None, alias="sizeLimit")
