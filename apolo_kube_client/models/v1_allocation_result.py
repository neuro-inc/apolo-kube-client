from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_device_allocation_result import V1DeviceAllocationResult
from .v1_node_selector import V1NodeSelector
from datetime import datetime

__all__ = ("V1AllocationResult",)


class V1AllocationResult(BaseModel):
    allocation_timestamp: datetime | None = Field(
        default_factory=lambda: None, alias="allocationTimestamp"
    )

    devices: V1DeviceAllocationResult = Field(
        default_factory=lambda: V1DeviceAllocationResult(), alias="devices"
    )

    node_selector: V1NodeSelector = Field(
        default_factory=lambda: V1NodeSelector(), alias="nodeSelector"
    )
