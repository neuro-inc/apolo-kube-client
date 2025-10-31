from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from .utils import _collection_if_none
from .v1_capacity_request_policy_range import V1CapacityRequestPolicyRange
from pydantic import BeforeValidator

__all__ = ("V1CapacityRequestPolicy",)


class V1CapacityRequestPolicy(BaseModel):
    """CapacityRequestPolicy defines how requests consume device capacity.

    Must not set more than one ValidRequestValues."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = (
        "io.k8s.api.resource.v1.CapacityRequestPolicy"
    )

    default: Annotated[
        str | None,
        Field(
            description="""Default specifies how much of this capacity is consumed by a request that does not contain an entry for it in DeviceRequest's Capacity.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    valid_range: Annotated[
        V1CapacityRequestPolicyRange | None,
        Field(
            alias="validRange",
            description="""ValidRange defines an acceptable quantity value range in consuming requests.

If this field is set, Default must be defined and it must fall within the defined ValidRange.

If the requested amount does not fall within the defined range, the request violates the policy, and this device cannot be allocated.

If the request doesn't contain this capacity entry, Default value is used.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    valid_values: Annotated[
        list[str],
        Field(
            alias="validValues",
            description="""ValidValues defines a set of acceptable quantity values in consuming requests.

Must not contain more than 10 entries. Must be sorted in ascending order.

If this field is set, Default must be defined and it must be included in ValidValues list.

If the requested amount does not match any valid value but smaller than some valid values, the scheduler calculates the smallest valid value that is greater than or equal to the request. That is: min(ceil(requestedValue) ∈ validValues), where requestedValue ≤ max(validValues).

If the requested amount exceeds all valid values, the request violates the policy, and this device cannot be allocated.""",
            exclude_if=lambda v: v == [],
        ),
        BeforeValidator(_collection_if_none("[]")),
    ] = []
