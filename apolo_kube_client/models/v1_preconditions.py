from __future__ import annotations

from pydantic import BaseModel, Field

__all__ = ("V1Preconditions",)


class V1Preconditions(BaseModel):
    resource_version: str | None = Field(None, alias="resourceVersion")

    uid: str | None = Field(None, alias="uid")
