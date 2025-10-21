from pydantic import AliasChoices, BaseModel, Field
from .utils import _collection_if_none
from .utils import _default_if_none
from .v1beta1_allocated_device_status import V1beta1AllocatedDeviceStatus
from .v1beta1_allocation_result import V1beta1AllocationResult
from .v1beta1_resource_claim_consumer_reference import (
    V1beta1ResourceClaimConsumerReference,
)
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1beta1ResourceClaimStatus",)


class V1beta1ResourceClaimStatus(BaseModel):
    allocation: Annotated[
        V1beta1AllocationResult,
        BeforeValidator(_default_if_none(V1beta1AllocationResult)),
    ] = Field(default_factory=lambda: V1beta1AllocationResult())

    devices: Annotated[
        list[V1beta1AllocatedDeviceStatus], BeforeValidator(_collection_if_none("[]"))
    ] = []

    reserved_for: Annotated[
        list[V1beta1ResourceClaimConsumerReference],
        BeforeValidator(_collection_if_none("[]")),
    ] = Field(
        default=[],
        serialization_alias="reservedFor",
        validation_alias=AliasChoices("reserved_for", "reservedFor"),
    )
