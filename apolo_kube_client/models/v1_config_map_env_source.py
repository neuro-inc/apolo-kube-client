from __future__ import annotations
from pydantic import BaseModel, Field


__all__ = ("V1ConfigMapEnvSource",)


class V1ConfigMapEnvSource(BaseModel):
    name: str | None = Field(default_factory=lambda: None, alias="name")

    optional: bool | None = Field(default_factory=lambda: None, alias="optional")
