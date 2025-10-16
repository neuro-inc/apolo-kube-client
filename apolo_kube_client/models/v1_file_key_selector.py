from __future__ import annotations
from pydantic import BaseModel, Field


__all__ = ("V1FileKeySelector",)


class V1FileKeySelector(BaseModel):
    key: str | None = Field(default_factory=lambda: None, alias="key")

    optional: bool | None = Field(default_factory=lambda: None, alias="optional")

    path: str | None = Field(default_factory=lambda: None, alias="path")

    volume_name: str | None = Field(default_factory=lambda: None, alias="volumeName")
