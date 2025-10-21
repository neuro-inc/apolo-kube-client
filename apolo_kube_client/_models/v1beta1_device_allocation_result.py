from pydantic import BaseModel
from .utils import _collection_if_none
from .v1beta1_device_allocation_configuration import (
    V1beta1DeviceAllocationConfiguration,
)
from .v1beta1_device_request_allocation_result import (
    V1beta1DeviceRequestAllocationResult,
)
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1beta1DeviceAllocationResult",)


class V1beta1DeviceAllocationResult(BaseModel):
    config: Annotated[
        list[V1beta1DeviceAllocationConfiguration],
        BeforeValidator(_collection_if_none("[]")),
    ] = []

    results: Annotated[
        list[V1beta1DeviceRequestAllocationResult],
        BeforeValidator(_collection_if_none("[]")),
    ] = []
