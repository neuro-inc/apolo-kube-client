from __future__ import annotations

from pydantic import BaseModel, Field

__all__ = ("V1ContainerImage",)


class V1ContainerImage(BaseModel):
    names: list[str] | None = Field(None, alias="names")

    size_bytes: int | None = Field(None, alias="sizeBytes")
