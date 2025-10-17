from __future__ import annotations
from pydantic import BaseModel, Field


__all__ = ("V1FileKeySelector",)


class V1FileKeySelector(BaseModel):
    key: str | None = Field(default_factory=lambda: None)

    optional: bool | None = Field(default_factory=lambda: None)

    path: str | None = Field(default_factory=lambda: None)

    volume_name: str | None = Field(default_factory=lambda: None, alias="volumeName")
