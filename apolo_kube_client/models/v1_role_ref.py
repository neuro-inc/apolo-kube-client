from __future__ import annotations
from pydantic import BaseModel, Field


__all__ = ("V1RoleRef",)


class V1RoleRef(BaseModel):
    api_group: str | None = Field(default_factory=lambda: None, alias="apiGroup")

    kind: str | None = Field(default_factory=lambda: None, alias="kind")

    name: str | None = Field(default_factory=lambda: None, alias="name")
