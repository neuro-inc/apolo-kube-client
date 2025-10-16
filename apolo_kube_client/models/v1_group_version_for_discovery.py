from __future__ import annotations

from pydantic import BaseModel, Field

__all__ = ("V1GroupVersionForDiscovery",)


class V1GroupVersionForDiscovery(BaseModel):
    group_version: str | None = Field(None, alias="groupVersion")

    version: str | None = Field(None, alias="version")
