from __future__ import annotations
from pydantic import BaseModel, Field
from .v1beta2_allocated_device_status import V1beta2AllocatedDeviceStatus
from .v1beta2_allocation_result import V1beta2AllocationResult
from .v1beta2_resource_claim_consumer_reference import (
    V1beta2ResourceClaimConsumerReference,
)

__all__ = ("V1beta2ResourceClaimStatus",)


class V1beta2ResourceClaimStatus(BaseModel):
    allocation: V1beta2AllocationResult = Field(
        default_factory=lambda: V1beta2AllocationResult(), alias="allocation"
    )

    devices: list[V1beta2AllocatedDeviceStatus] = Field(
        default_factory=lambda: [], alias="devices"
    )

    reserved_for: list[V1beta2ResourceClaimConsumerReference] = Field(
        default_factory=lambda: [], alias="reservedFor"
    )
