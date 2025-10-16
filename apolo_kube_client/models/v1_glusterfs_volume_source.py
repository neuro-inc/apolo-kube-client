from __future__ import annotations

from pydantic import BaseModel, Field

__all__ = ("V1GlusterfsVolumeSource",)


class V1GlusterfsVolumeSource(BaseModel):
    endpoints: str | None = Field(None, alias="endpoints")

    path: str | None = Field(None, alias="path")

    read_only: bool | None = Field(None, alias="readOnly")
