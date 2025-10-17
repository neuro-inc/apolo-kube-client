from __future__ import annotations
from pydantic import BaseModel, Field


__all__ = ("V1beta1ParentReference",)


class V1beta1ParentReference(BaseModel):
    group: str | None = Field(default_factory=lambda: None)

    name: str | None = Field(default_factory=lambda: None)

    namespace: str | None = Field(default_factory=lambda: None)

    resource: str | None = Field(default_factory=lambda: None)
