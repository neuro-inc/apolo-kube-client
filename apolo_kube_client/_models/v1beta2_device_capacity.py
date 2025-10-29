from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from .utils import _default_if_none
from .v1beta2_capacity_request_policy import V1beta2CapacityRequestPolicy
from pydantic import BeforeValidator

__all__ = ("V1beta2DeviceCapacity",)


class V1beta2DeviceCapacity(BaseModel):
    """DeviceCapacity describes a quantity associated with a device."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.resource.v1beta2.DeviceCapacity"

    request_policy: Annotated[
        V1beta2CapacityRequestPolicy,
        Field(
            alias="requestPolicy",
            description="""RequestPolicy defines how this DeviceCapacity must be consumed when the device is allowed to be shared by multiple allocations.

The Device must have allowMultipleAllocations set to true in order to set a requestPolicy.

If unset, capacity requests are unconstrained: requests can consume any amount of capacity, as long as the total consumed across all allocations does not exceed the device's defined capacity. If request is also unset, default is the full capacity value.""",
            exclude_if=lambda v: not v.__pydantic_fields_set__,
        ),
        BeforeValidator(_default_if_none(V1beta2CapacityRequestPolicy)),
    ] = V1beta2CapacityRequestPolicy()

    value: Annotated[
        str,
        Field(
            description="""Value defines how much of a certain capacity that device has.

This field reflects the fixed total capacity and does not change. The consumed amount is tracked separately by scheduler and does not affect this value."""
        ),
    ]
