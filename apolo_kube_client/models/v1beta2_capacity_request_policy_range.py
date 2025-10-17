from __future__ import annotations
from pydantic import BaseModel, Field


__all__ = ("V1beta2CapacityRequestPolicyRange",)


class V1beta2CapacityRequestPolicyRange(BaseModel):
    max: str | None = Field(default=None)

    min: str | None = Field(default=None)

    step: str | None = Field(default=None)
