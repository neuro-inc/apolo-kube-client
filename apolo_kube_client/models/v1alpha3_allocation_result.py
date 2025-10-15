from pydantic import BaseModel, Field

from .v1_node_selector import V1NodeSelector
from .v1alpha3_device_allocation_result import V1alpha3DeviceAllocationResult


class V1alpha3AllocationResult(BaseModel):
    devices: V1alpha3DeviceAllocationResult | None = Field(None, alias="devices")

    node_selector: V1NodeSelector | None = Field(None, alias="nodeSelector")
