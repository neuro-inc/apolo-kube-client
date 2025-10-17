from __future__ import annotations
from pydantic import BaseModel, Field


__all__ = ("V1NodeAddress",)


class V1NodeAddress(BaseModel):
    address: str | None = Field(default_factory=lambda: None)

    type: str | None = Field(default_factory=lambda: None)
