from __future__ import annotations
from pydantic import BaseModel, Field


__all__ = ("V1BoundObjectReference",)


class V1BoundObjectReference(BaseModel):
    api_version: str | None = Field(default_factory=lambda: None, alias="apiVersion")

    kind: str | None = Field(default_factory=lambda: None)

    name: str | None = Field(default_factory=lambda: None)

    uid: str | None = Field(default_factory=lambda: None)
