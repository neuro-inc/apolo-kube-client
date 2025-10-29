from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from .utils import _collection_if_none
from .utils import _default_if_none
from .v1_allocated_device_status import V1AllocatedDeviceStatus
from .v1_allocation_result import V1AllocationResult
from .v1_resource_claim_consumer_reference import V1ResourceClaimConsumerReference
from pydantic import BeforeValidator

__all__ = ("V1ResourceClaimStatus",)


class V1ResourceClaimStatus(BaseModel):
    """ResourceClaimStatus tracks whether the resource has been allocated and what the result of that was."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.resource.v1.ResourceClaimStatus"

    allocation: Annotated[
        V1AllocationResult,
        Field(
            description="""Allocation is set once the claim has been allocated successfully.""",
            exclude_if=lambda v: not v.__pydantic_fields_set__,
        ),
        BeforeValidator(_default_if_none(V1AllocationResult)),
    ] = V1AllocationResult()

    devices: Annotated[
        list[V1AllocatedDeviceStatus],
        Field(
            description="""Devices contains the status of each device allocated for this claim, as reported by the driver. This can include driver-specific information. Entries are owned by their respective drivers.""",
            exclude_if=lambda v: v == [],
        ),
        BeforeValidator(_collection_if_none("[]")),
    ] = []

    reserved_for: Annotated[
        list[V1ResourceClaimConsumerReference],
        Field(
            alias="reservedFor",
            description="""ReservedFor indicates which entities are currently allowed to use the claim. A Pod which references a ResourceClaim which is not reserved for that Pod will not be started. A claim that is in use or might be in use because it has been reserved must not get deallocated.

In a cluster with multiple scheduler instances, two pods might get scheduled concurrently by different schedulers. When they reference the same ResourceClaim which already has reached its maximum number of consumers, only one pod can be scheduled.

Both schedulers try to add their pod to the claim.status.reservedFor field, but only the update that reaches the API server first gets stored. The other one fails with an error and the scheduler which issued it knows that it must put the pod back into the queue, waiting for the ResourceClaim to become usable again.

There can be at most 256 such reservations. This may get increased in the future, but not reduced.""",
            exclude_if=lambda v: v == [],
        ),
        BeforeValidator(_collection_if_none("[]")),
    ] = []
