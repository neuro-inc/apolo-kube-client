from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field
from .v1_node_selector import V1NodeSelector
from .v1beta1_device_allocation_result import V1beta1DeviceAllocationResult
from datetime import datetime

__all__ = ("V1beta1AllocationResult",)


class V1beta1AllocationResult(BaseModel):
    allocation_timestamp: datetime | None = Field(
        default=None,
        serialization_alias="allocationTimestamp",
        validation_alias=AliasChoices("allocation_timestamp", "allocationTimestamp"),
    )

    devices: V1beta1DeviceAllocationResult = Field(
        default_factory=lambda: V1beta1DeviceAllocationResult()
    )

    node_selector: V1NodeSelector = Field(
        default_factory=lambda: V1NodeSelector(),
        serialization_alias="nodeSelector",
        validation_alias=AliasChoices("node_selector", "nodeSelector"),
    )
