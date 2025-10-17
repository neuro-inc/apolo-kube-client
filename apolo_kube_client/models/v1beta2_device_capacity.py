from __future__ import annotations
from pydantic import BaseModel, Field
from .v1beta2_capacity_request_policy import V1beta2CapacityRequestPolicy

__all__ = ("V1beta2DeviceCapacity",)


class V1beta2DeviceCapacity(BaseModel):
    request_policy: V1beta2CapacityRequestPolicy = Field(
        default_factory=lambda: V1beta2CapacityRequestPolicy(), alias="requestPolicy"
    )

    value: str | None = Field(default_factory=lambda: None)
