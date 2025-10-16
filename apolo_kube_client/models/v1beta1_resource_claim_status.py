from __future__ import annotations

from pydantic import BaseModel, Field

from .v1beta1_allocated_device_status import V1beta1AllocatedDeviceStatus
from .v1beta1_allocation_result import V1beta1AllocationResult
from .v1beta1_resource_claim_consumer_reference import (
    V1beta1ResourceClaimConsumerReference,
)

__all__ = ("V1beta1ResourceClaimStatus",)


class V1beta1ResourceClaimStatus(BaseModel):
    allocation: V1beta1AllocationResult | None = Field(None, alias="allocation")

    devices: list[V1beta1AllocatedDeviceStatus] | None = Field(None, alias="devices")

    reserved_for: list[V1beta1ResourceClaimConsumerReference] | None = Field(
        None, alias="reservedFor"
    )
