from __future__ import annotations
from pydantic import BaseModel, Field
from .v1beta1_device_claim_configuration import V1beta1DeviceClaimConfiguration
from .v1beta1_device_constraint import V1beta1DeviceConstraint
from .v1beta1_device_request import V1beta1DeviceRequest

__all__ = ("V1beta1DeviceClaim",)


class V1beta1DeviceClaim(BaseModel):
    config: list[V1beta1DeviceClaimConfiguration] = Field(default=[])

    constraints: list[V1beta1DeviceConstraint] = Field(default=[])

    requests: list[V1beta1DeviceRequest] = Field(default=[])
