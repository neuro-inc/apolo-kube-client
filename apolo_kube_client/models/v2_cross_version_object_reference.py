from __future__ import annotations

from pydantic import BaseModel, Field

__all__ = ("V2CrossVersionObjectReference",)


class V2CrossVersionObjectReference(BaseModel):
    api_version: str | None = Field(None, alias="apiVersion")

    kind: str | None = Field(None, alias="kind")

    name: str | None = Field(None, alias="name")
