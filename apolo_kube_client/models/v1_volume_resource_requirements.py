from __future__ import annotations
from pydantic import BaseModel, Field


__all__ = ("V1VolumeResourceRequirements",)


class V1VolumeResourceRequirements(BaseModel):
    limits: dict[str, str] = Field(default_factory=lambda: {})

    requests: dict[str, str] = Field(default_factory=lambda: {})
