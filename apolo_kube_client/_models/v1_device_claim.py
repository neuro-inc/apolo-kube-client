from pydantic import BaseModel
from .v1_device_claim_configuration import V1DeviceClaimConfiguration
from .v1_device_constraint import V1DeviceConstraint
from .v1_device_request import V1DeviceRequest

__all__ = ("V1DeviceClaim",)


class V1DeviceClaim(BaseModel):
    config: list[V1DeviceClaimConfiguration] = []

    constraints: list[V1DeviceConstraint] = []

    requests: list[V1DeviceRequest] = []
