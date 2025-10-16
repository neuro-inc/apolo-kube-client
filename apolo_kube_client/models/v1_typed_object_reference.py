from __future__ import annotations
from pydantic import BaseModel, Field


__all__ = ("V1TypedObjectReference",)


class V1TypedObjectReference(BaseModel):
    api_group: str | None = Field(default_factory=lambda: None, alias="apiGroup")

    kind: str | None = Field(default_factory=lambda: None, alias="kind")

    name: str | None = Field(default_factory=lambda: None, alias="name")

    namespace: str | None = Field(default_factory=lambda: None, alias="namespace")
