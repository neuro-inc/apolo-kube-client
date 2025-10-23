from pydantic import AliasChoices, BaseModel, Field
from .utils import _collection_if_none
from .utils import _default_if_none
from .utils import _exclude_if
from .v1beta2_allocated_device_status import V1beta2AllocatedDeviceStatus
from .v1beta2_allocation_result import V1beta2AllocationResult
from .v1beta2_resource_claim_consumer_reference import (
    V1beta2ResourceClaimConsumerReference,
)
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1beta2ResourceClaimStatus",)


class V1beta2ResourceClaimStatus(BaseModel):
    allocation: Annotated[
        V1beta2AllocationResult,
        BeforeValidator(_default_if_none(V1beta2AllocationResult)),
    ] = Field(default_factory=lambda: V1beta2AllocationResult(), exclude_if=_exclude_if)

    devices: Annotated[
        list[V1beta2AllocatedDeviceStatus], BeforeValidator(_collection_if_none("[]"))
    ] = Field(default=[], exclude_if=_exclude_if)

    reserved_for: Annotated[
        list[V1beta2ResourceClaimConsumerReference],
        BeforeValidator(_collection_if_none("[]")),
    ] = Field(
        default=[],
        serialization_alias="reservedFor",
        validation_alias=AliasChoices("reserved_for", "reservedFor"),
        exclude_if=_exclude_if,
    )
