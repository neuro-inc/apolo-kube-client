from __future__ import annotations
from pydantic import BaseModel, Field
from .v1beta1_device_allocation_configuration import (
    V1beta1DeviceAllocationConfiguration,
)
from .v1beta1_device_request_allocation_result import (
    V1beta1DeviceRequestAllocationResult,
)

__all__ = ("V1beta1DeviceAllocationResult",)


class V1beta1DeviceAllocationResult(BaseModel):
    config: list[V1beta1DeviceAllocationConfiguration] = Field(
        default_factory=lambda: [], alias="config"
    )

    results: list[V1beta1DeviceRequestAllocationResult] = Field(
        default_factory=lambda: [], alias="results"
    )
