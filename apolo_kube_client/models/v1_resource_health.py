from __future__ import annotations

from pydantic import BaseModel, Field

__all__ = ("V1ResourceHealth",)


class V1ResourceHealth(BaseModel):
    health: str | None = Field(None, alias="health")

    resource_id: str | None = Field(None, alias="resourceID")
