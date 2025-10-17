from __future__ import annotations
from pydantic import BaseModel, Field


__all__ = ("V1CapacityRequestPolicyRange",)


class V1CapacityRequestPolicyRange(BaseModel):
    max: str | None = Field(default_factory=lambda: None)

    min: str | None = Field(default_factory=lambda: None)

    step: str | None = Field(default_factory=lambda: None)
