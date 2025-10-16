from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_device_allocation_configuration import V1DeviceAllocationConfiguration
from .v1_device_request_allocation_result import V1DeviceRequestAllocationResult

__all__ = ("V1DeviceAllocationResult",)


class V1DeviceAllocationResult(BaseModel):
    config: list[V1DeviceAllocationConfiguration] = Field(
        default_factory=lambda: [], alias="config"
    )

    results: list[V1DeviceRequestAllocationResult] = Field(
        default_factory=lambda: [], alias="results"
    )
