from pydantic import BaseModel, Field

from .v1alpha3_device_claim_configuration import V1alpha3DeviceClaimConfiguration
from .v1alpha3_device_constraint import V1alpha3DeviceConstraint
from .v1alpha3_device_request import V1alpha3DeviceRequest


class V1alpha3DeviceClaim(BaseModel):
    config: list[V1alpha3DeviceClaimConfiguration] | None = Field(None, alias="config")

    constraints: list[V1alpha3DeviceConstraint] | None = Field(
        None, alias="constraints"
    )

    requests: list[V1alpha3DeviceRequest] | None = Field(None, alias="requests")
