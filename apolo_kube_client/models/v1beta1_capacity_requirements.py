from __future__ import annotations
from pydantic import BaseModel, Field


__all__ = ("V1beta1CapacityRequirements",)


class V1beta1CapacityRequirements(BaseModel):
    requests: dict[str, str] = Field(default_factory=lambda: {}, alias="requests")
