from __future__ import annotations
from pydantic import BaseModel, Field
from .v1beta1_capacity_request_policy import V1beta1CapacityRequestPolicy

__all__ = ("V1beta1DeviceCapacity",)


class V1beta1DeviceCapacity(BaseModel):
    request_policy: V1beta1CapacityRequestPolicy = Field(
        default_factory=lambda: V1beta1CapacityRequestPolicy(), alias="requestPolicy"
    )

    value: str | None = Field(default_factory=lambda: None)
