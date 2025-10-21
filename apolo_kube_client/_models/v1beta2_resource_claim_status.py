from pydantic import AliasChoices, BaseModel, Field
from .base import _default_if_none
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
    ] = Field(default_factory=lambda: V1beta2AllocationResult())

    devices: list[V1beta2AllocatedDeviceStatus] = []

    reserved_for: list[V1beta2ResourceClaimConsumerReference] = Field(
        default=[],
        serialization_alias="reservedFor",
        validation_alias=AliasChoices("reserved_for", "reservedFor"),
    )
