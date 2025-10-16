from __future__ import annotations

from pydantic import BaseModel, Field

from .v1_node_selector import V1NodeSelector
from .v1beta1_device_allocation_result import V1beta1DeviceAllocationResult

__all__ = ("V1beta1AllocationResult",)


class V1beta1AllocationResult(BaseModel):
    devices: V1beta1DeviceAllocationResult | None = Field(None, alias="devices")

    node_selector: V1NodeSelector | None = Field(None, alias="nodeSelector")
