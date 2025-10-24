from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from .utils import _collection_if_none
from pydantic import BeforeValidator

__all__ = ("V1beta2CapacityRequirements",)


class V1beta2CapacityRequirements(BaseModel):
    """CapacityRequirements defines the capacity requirements for a specific device request."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = (
        "io.k8s.api.resource.v1beta2.CapacityRequirements"
    )

    requests: Annotated[
        dict[str, str],
        Field(
            description="""Requests represent individual device resource requests for distinct resources, all of which must be provided by the device.

This value is used as an additional filtering condition against the available capacity on the device. This is semantically equivalent to a CEL selector with `device.capacity[<domain>].<name>.compareTo(quantity(<request quantity>)) >= 0`. For example, device.capacity['test-driver.cdi.k8s.io'].counters.compareTo(quantity('2')) >= 0.

When a requestPolicy is defined, the requested amount is adjusted upward to the nearest valid value based on the policy. If the requested amount cannot be adjusted to a valid value—because it exceeds what the requestPolicy allows— the device is considered ineligible for allocation.

For any capacity that is not explicitly requested: - If no requestPolicy is set, the default consumed capacity is equal to the full device capacity
  (i.e., the whole device is claimed).
- If a requestPolicy is set, the default consumed capacity is determined according to that policy.

If the device allows multiple allocation, the aggregated amount across all requests must not exceed the capacity value. The consumed capacity, which may be adjusted based on the requestPolicy if defined, is recorded in the resource claim’s status.devices[*].consumedCapacity field.""",
            exclude_if=lambda v: v == {},
        ),
        BeforeValidator(_collection_if_none("{}")),
    ] = {}
