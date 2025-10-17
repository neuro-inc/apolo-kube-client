from __future__ import annotations
from pydantic import BaseModel, Field


__all__ = ("V1NFSVolumeSource",)


class V1NFSVolumeSource(BaseModel):
    path: str | None = Field(default_factory=lambda: None)

    read_only: bool | None = Field(default_factory=lambda: None, alias="readOnly")

    server: str | None = Field(default_factory=lambda: None)
