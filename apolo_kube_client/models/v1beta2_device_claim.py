from __future__ import annotations
from pydantic import BaseModel, Field
from .v1beta2_device_claim_configuration import V1beta2DeviceClaimConfiguration
from .v1beta2_device_constraint import V1beta2DeviceConstraint
from .v1beta2_device_request import V1beta2DeviceRequest

__all__ = ("V1beta2DeviceClaim",)


class V1beta2DeviceClaim(BaseModel):
    config: list[V1beta2DeviceClaimConfiguration] = Field(
        default_factory=lambda: [], alias="config"
    )

    constraints: list[V1beta2DeviceConstraint] = Field(
        default_factory=lambda: [], alias="constraints"
    )

    requests: list[V1beta2DeviceRequest] = Field(
        default_factory=lambda: [], alias="requests"
    )
