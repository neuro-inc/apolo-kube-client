from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field
from .v1_allocated_device_status import V1AllocatedDeviceStatus
from .v1_allocation_result import V1AllocationResult
from .v1_resource_claim_consumer_reference import V1ResourceClaimConsumerReference

__all__ = ("V1ResourceClaimStatus",)


class V1ResourceClaimStatus(BaseModel):
    allocation: V1AllocationResult = Field(default_factory=lambda: V1AllocationResult())

    devices: list[V1AllocatedDeviceStatus] = Field(default=[])

    reserved_for: list[V1ResourceClaimConsumerReference] = Field(
        default=[],
        serialization_alias="reservedFor",
        validation_alias=AliasChoices("reserved_for", "reservedFor"),
    )
