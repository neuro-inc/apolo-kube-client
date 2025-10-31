from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from .utils import _default_if_none
from .v1_node_selector import V1NodeSelector
from .v1beta2_device_allocation_result import V1beta2DeviceAllocationResult
from datetime import datetime
from pydantic import BeforeValidator

__all__ = ("V1beta2AllocationResult",)


class V1beta2AllocationResult(BaseModel):
    """AllocationResult contains attributes of an allocated resource."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = (
        "io.k8s.api.resource.v1beta2.AllocationResult"
    )

    allocation_timestamp: Annotated[
        datetime | None,
        Field(
            alias="allocationTimestamp",
            description="""AllocationTimestamp stores the time when the resources were allocated. This field is not guaranteed to be set, in which case that time is unknown.

This is an alpha field and requires enabling the DRADeviceBindingConditions and DRAResourceClaimDeviceStatus feature gate.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    devices: Annotated[
        V1beta2DeviceAllocationResult,
        Field(
            description="""Devices is the result of allocating devices.""",
            exclude_if=lambda v: not v.__pydantic_fields_set__,
        ),
        BeforeValidator(_default_if_none(V1beta2DeviceAllocationResult)),
    ] = V1beta2DeviceAllocationResult()

    node_selector: Annotated[
        V1NodeSelector | None,
        Field(
            alias="nodeSelector",
            description="""NodeSelector defines where the allocated resources are available. If unset, they are available everywhere.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None
