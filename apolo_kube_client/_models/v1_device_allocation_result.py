from pydantic import BaseModel
from .utils import _collection_if_none
from .v1_device_allocation_configuration import V1DeviceAllocationConfiguration
from .v1_device_request_allocation_result import V1DeviceRequestAllocationResult
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1DeviceAllocationResult",)


class V1DeviceAllocationResult(BaseModel):
    config: Annotated[
        list[V1DeviceAllocationConfiguration],
        BeforeValidator(_collection_if_none("[]")),
    ] = []

    results: Annotated[
        list[V1DeviceRequestAllocationResult],
        BeforeValidator(_collection_if_none("[]")),
    ] = []
