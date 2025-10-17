from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_device_claim_configuration import V1DeviceClaimConfiguration
from .v1_device_constraint import V1DeviceConstraint
from .v1_device_request import V1DeviceRequest

__all__ = ("V1DeviceClaim",)


class V1DeviceClaim(BaseModel):
    config: list[V1DeviceClaimConfiguration] = Field(default_factory=lambda: [])

    constraints: list[V1DeviceConstraint] = Field(default_factory=lambda: [])

    requests: list[V1DeviceRequest] = Field(default_factory=lambda: [])
