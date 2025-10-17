from pydantic import BaseModel
from .v1_device_allocation_configuration import V1DeviceAllocationConfiguration
from .v1_device_request_allocation_result import V1DeviceRequestAllocationResult

__all__ = ("V1DeviceAllocationResult",)


class V1DeviceAllocationResult(BaseModel):
    config: list[V1DeviceAllocationConfiguration] = []

    results: list[V1DeviceRequestAllocationResult] = []
