from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_node_selector import V1NodeSelector
from .v1beta2_device_allocation_result import V1beta2DeviceAllocationResult
from datetime import datetime

__all__ = ("V1beta2AllocationResult",)


class V1beta2AllocationResult(BaseModel):
    allocation_timestamp: datetime | None = Field(
        default_factory=lambda: None, alias="allocationTimestamp"
    )

    devices: V1beta2DeviceAllocationResult = Field(
        default_factory=lambda: V1beta2DeviceAllocationResult(), alias="devices"
    )

    node_selector: V1NodeSelector = Field(
        default_factory=lambda: V1NodeSelector(), alias="nodeSelector"
    )
