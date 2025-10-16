from __future__ import annotations

from pydantic import BaseModel, Field

__all__ = ("V1ResourceClaim",)


class V1ResourceClaim(BaseModel):
    name: str | None = Field(None, alias="name")

    request: str | None = Field(None, alias="request")
