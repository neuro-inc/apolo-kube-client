from pydantic import BaseModel, Field
from .utils import _collection_if_none
from .utils import _exclude_if
from .v1_device_allocation_configuration import V1DeviceAllocationConfiguration
from .v1_device_request_allocation_result import V1DeviceRequestAllocationResult
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1DeviceAllocationResult",)


class V1DeviceAllocationResult(BaseModel):
    config: Annotated[
        list[V1DeviceAllocationConfiguration],
        BeforeValidator(_collection_if_none("[]")),
    ] = Field(default=[], exclude_if=_exclude_if)

    results: Annotated[
        list[V1DeviceRequestAllocationResult],
        BeforeValidator(_collection_if_none("[]")),
    ] = Field(default=[], exclude_if=_exclude_if)
