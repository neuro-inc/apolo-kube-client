from pydantic import BaseModel, Field

from .v1alpha3_device_allocation_configuration import (
    V1alpha3DeviceAllocationConfiguration,
)
from .v1alpha3_device_request_allocation_result import (
    V1alpha3DeviceRequestAllocationResult,
)


class V1alpha3DeviceAllocationResult(BaseModel):
    config: list[V1alpha3DeviceAllocationConfiguration] | None = Field(
        None, alias="config"
    )

    results: list[V1alpha3DeviceRequestAllocationResult] | None = Field(
        None, alias="results"
    )
