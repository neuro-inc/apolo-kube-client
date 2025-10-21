from pydantic import BaseModel
from .utils import _collection_if_none
from .v1beta2_device_allocation_configuration import (
    V1beta2DeviceAllocationConfiguration,
)
from .v1beta2_device_request_allocation_result import (
    V1beta2DeviceRequestAllocationResult,
)
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1beta2DeviceAllocationResult",)


class V1beta2DeviceAllocationResult(BaseModel):
    config: Annotated[
        list[V1beta2DeviceAllocationConfiguration],
        BeforeValidator(_collection_if_none("[]")),
    ] = []

    results: Annotated[
        list[V1beta2DeviceRequestAllocationResult],
        BeforeValidator(_collection_if_none("[]")),
    ] = []
