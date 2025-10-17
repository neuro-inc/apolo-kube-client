from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field
from .v1beta2_allocated_device_status import V1beta2AllocatedDeviceStatus
from .v1beta2_allocation_result import V1beta2AllocationResult
from .v1beta2_resource_claim_consumer_reference import (
    V1beta2ResourceClaimConsumerReference,
)

__all__ = ("V1beta2ResourceClaimStatus",)


class V1beta2ResourceClaimStatus(BaseModel):
    allocation: V1beta2AllocationResult = Field(
        default_factory=lambda: V1beta2AllocationResult()
    )

    devices: list[V1beta2AllocatedDeviceStatus] = Field(default=[])

    reserved_for: list[V1beta2ResourceClaimConsumerReference] = Field(
        default=[],
        serialization_alias="reservedFor",
        validation_alias=AliasChoices("reserved_for", "reservedFor"),
    )
