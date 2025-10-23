from pydantic import BaseModel, Field
from .utils import _collection_if_none
from .utils import _exclude_if
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
    ] = Field(default=[], exclude_if=_exclude_if)

    results: Annotated[
        list[V1beta2DeviceRequestAllocationResult],
        BeforeValidator(_collection_if_none("[]")),
    ] = Field(default=[], exclude_if=_exclude_if)
