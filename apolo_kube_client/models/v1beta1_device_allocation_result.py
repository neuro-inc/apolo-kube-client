from pydantic import BaseModel
from .v1beta1_device_allocation_configuration import (
    V1beta1DeviceAllocationConfiguration,
)
from .v1beta1_device_request_allocation_result import (
    V1beta1DeviceRequestAllocationResult,
)

__all__ = ("V1beta1DeviceAllocationResult",)


class V1beta1DeviceAllocationResult(BaseModel):
    config: list[V1beta1DeviceAllocationConfiguration] = []

    results: list[V1beta1DeviceRequestAllocationResult] = []
