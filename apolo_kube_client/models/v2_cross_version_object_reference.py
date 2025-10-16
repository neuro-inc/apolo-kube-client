from __future__ import annotations
from pydantic import BaseModel, Field


__all__ = ("V2CrossVersionObjectReference",)


class V2CrossVersionObjectReference(BaseModel):
    api_version: str | None = Field(default_factory=lambda: None, alias="apiVersion")

    kind: str | None = Field(default_factory=lambda: None, alias="kind")

    name: str | None = Field(default_factory=lambda: None, alias="name")
