from __future__ import annotations
from pydantic import BaseModel, Field


__all__ = ("CoreV1ResourceClaim",)


class CoreV1ResourceClaim(BaseModel):
    name: str | None = Field(default=None)

    request: str | None = Field(default=None)
