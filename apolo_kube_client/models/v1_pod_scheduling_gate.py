from __future__ import annotations

from pydantic import BaseModel, Field

__all__ = ("V1PodSchedulingGate",)


class V1PodSchedulingGate(BaseModel):
    name: str | None = Field(None, alias="name")
