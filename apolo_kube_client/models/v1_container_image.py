from __future__ import annotations
from pydantic import BaseModel, Field


__all__ = ("V1ContainerImage",)


class V1ContainerImage(BaseModel):
    names: list[str] = Field(default_factory=lambda: [])

    size_bytes: int | None = Field(default_factory=lambda: None, alias="sizeBytes")
