from pydantic import BaseModel
from .v1beta1_device_claim_configuration import V1beta1DeviceClaimConfiguration
from .v1beta1_device_constraint import V1beta1DeviceConstraint
from .v1beta1_device_request import V1beta1DeviceRequest

__all__ = ("V1beta1DeviceClaim",)


class V1beta1DeviceClaim(BaseModel):
    config: list[V1beta1DeviceClaimConfiguration] = []

    constraints: list[V1beta1DeviceConstraint] = []

    requests: list[V1beta1DeviceRequest] = []
