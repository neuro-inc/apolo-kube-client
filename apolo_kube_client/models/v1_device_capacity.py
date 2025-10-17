from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_capacity_request_policy import V1CapacityRequestPolicy

__all__ = ("V1DeviceCapacity",)


class V1DeviceCapacity(BaseModel):
    request_policy: V1CapacityRequestPolicy = Field(
        default_factory=lambda: V1CapacityRequestPolicy(), alias="requestPolicy"
    )

    value: str | None = Field(default_factory=lambda: None)
