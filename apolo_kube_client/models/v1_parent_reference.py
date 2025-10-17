from __future__ import annotations
from pydantic import BaseModel, Field


__all__ = ("V1ParentReference",)


class V1ParentReference(BaseModel):
    group: str | None = Field(default=None)

    name: str | None = Field(default=None)

    namespace: str | None = Field(default=None)

    resource: str | None = Field(default=None)
