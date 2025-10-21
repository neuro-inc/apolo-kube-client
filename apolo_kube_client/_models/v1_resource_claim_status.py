from pydantic import AliasChoices, BaseModel, Field
from .utils import _collection_if_none
from .utils import _default_if_none
from .v1_allocated_device_status import V1AllocatedDeviceStatus
from .v1_allocation_result import V1AllocationResult
from .v1_resource_claim_consumer_reference import V1ResourceClaimConsumerReference
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1ResourceClaimStatus",)


class V1ResourceClaimStatus(BaseModel):
    allocation: Annotated[
        V1AllocationResult, BeforeValidator(_default_if_none(V1AllocationResult))
    ] = Field(default_factory=lambda: V1AllocationResult())

    devices: Annotated[
        list[V1AllocatedDeviceStatus], BeforeValidator(_collection_if_none("[]"))
    ] = []

    reserved_for: Annotated[
        list[V1ResourceClaimConsumerReference],
        BeforeValidator(_collection_if_none("[]")),
    ] = Field(
        default=[],
        serialization_alias="reservedFor",
        validation_alias=AliasChoices("reserved_for", "reservedFor"),
    )
