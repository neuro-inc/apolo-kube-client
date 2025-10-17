from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field
from .v1beta1_allocated_device_status import V1beta1AllocatedDeviceStatus
from .v1beta1_allocation_result import V1beta1AllocationResult
from .v1beta1_resource_claim_consumer_reference import (
    V1beta1ResourceClaimConsumerReference,
)

__all__ = ("V1beta1ResourceClaimStatus",)


class V1beta1ResourceClaimStatus(BaseModel):
    allocation: V1beta1AllocationResult = Field(
        default_factory=lambda: V1beta1AllocationResult()
    )

    devices: list[V1beta1AllocatedDeviceStatus] = Field(default=[])

    reserved_for: list[V1beta1ResourceClaimConsumerReference] = Field(
        default=[],
        serialization_alias="reservedFor",
        validation_alias=AliasChoices("reserved_for", "reservedFor"),
    )
