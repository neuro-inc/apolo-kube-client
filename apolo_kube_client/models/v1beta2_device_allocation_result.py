from __future__ import annotations
from pydantic import BaseModel, Field
from .v1beta2_device_allocation_configuration import (
    V1beta2DeviceAllocationConfiguration,
)
from .v1beta2_device_request_allocation_result import (
    V1beta2DeviceRequestAllocationResult,
)

__all__ = ("V1beta2DeviceAllocationResult",)


class V1beta2DeviceAllocationResult(BaseModel):
    config: list[V1beta2DeviceAllocationConfiguration] = Field(
        default_factory=lambda: [], alias="config"
    )

    results: list[V1beta2DeviceRequestAllocationResult] = Field(
        default_factory=lambda: [], alias="results"
    )
