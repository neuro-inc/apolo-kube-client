from __future__ import annotations
from pydantic import BaseModel, Field


__all__ = ("V1TypedLocalObjectReference",)


class V1TypedLocalObjectReference(BaseModel):
    api_group: str | None = Field(default_factory=lambda: None, alias="apiGroup")

    kind: str | None = Field(default_factory=lambda: None)

    name: str | None = Field(default_factory=lambda: None)
