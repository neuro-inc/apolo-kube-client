from __future__ import annotations
from pydantic import BaseModel, Field


__all__ = ("V1CapacityRequestPolicyRange",)


class V1CapacityRequestPolicyRange(BaseModel):
    max: str | None = Field(default=None)

    min: str | None = Field(default=None)

    step: str | None = Field(default=None)
