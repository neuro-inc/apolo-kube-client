from __future__ import annotations
from pydantic import BaseModel, Field


__all__ = ("V1beta2CapacityRequirements",)


class V1beta2CapacityRequirements(BaseModel):
    requests: dict[str, str] = Field(default_factory=lambda: {}, alias="requests")
