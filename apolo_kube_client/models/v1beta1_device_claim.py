from pydantic import BaseModel, Field

from .v1beta1_device_claim_configuration import V1beta1DeviceClaimConfiguration
from .v1beta1_device_constraint import V1beta1DeviceConstraint
from .v1beta1_device_request import V1beta1DeviceRequest


class V1beta1DeviceClaim(BaseModel):
    config: list[V1beta1DeviceClaimConfiguration] | None = Field(None, alias="config")

    constraints: list[V1beta1DeviceConstraint] | None = Field(None, alias="constraints")

    requests: list[V1beta1DeviceRequest] | None = Field(None, alias="requests")
