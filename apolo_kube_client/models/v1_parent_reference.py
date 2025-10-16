from __future__ import annotations
from pydantic import BaseModel, Field


__all__ = ("V1ParentReference",)


class V1ParentReference(BaseModel):
    group: str | None = Field(default_factory=lambda: None, alias="group")

    name: str | None = Field(default_factory=lambda: None, alias="name")

    namespace: str | None = Field(default_factory=lambda: None, alias="namespace")

    resource: str | None = Field(default_factory=lambda: None, alias="resource")
