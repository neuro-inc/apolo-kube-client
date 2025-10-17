from __future__ import annotations
from pydantic import BaseModel, Field


__all__ = ("V1NodeSwapStatus",)


class V1NodeSwapStatus(BaseModel):
    capacity: int | None = Field(default_factory=lambda: None)
