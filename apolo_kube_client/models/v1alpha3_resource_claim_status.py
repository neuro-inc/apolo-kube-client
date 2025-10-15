from pydantic import BaseModel, Field

from .v1alpha3_allocated_device_status import V1alpha3AllocatedDeviceStatus
from .v1alpha3_allocation_result import V1alpha3AllocationResult
from .v1alpha3_resource_claim_consumer_reference import (
    V1alpha3ResourceClaimConsumerReference,
)


class V1alpha3ResourceClaimStatus(BaseModel):
    allocation: V1alpha3AllocationResult | None = Field(None, alias="allocation")

    devices: list[V1alpha3AllocatedDeviceStatus] | None = Field(None, alias="devices")

    reserved_for: list[V1alpha3ResourceClaimConsumerReference] | None = Field(
        None, alias="reservedFor"
    )
