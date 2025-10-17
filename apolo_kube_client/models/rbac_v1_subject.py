from __future__ import annotations
from pydantic import BaseModel, Field


__all__ = ("RbacV1Subject",)


class RbacV1Subject(BaseModel):
    api_group: str | None = Field(default_factory=lambda: None, alias="apiGroup")

    kind: str | None = Field(default_factory=lambda: None)

    name: str | None = Field(default_factory=lambda: None)

    namespace: str | None = Field(default_factory=lambda: None)
