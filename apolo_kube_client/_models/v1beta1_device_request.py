from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from .utils import _collection_if_none
from .utils import _default_if_none
from .v1beta1_capacity_requirements import V1beta1CapacityRequirements
from .v1beta1_device_selector import V1beta1DeviceSelector
from .v1beta1_device_sub_request import V1beta1DeviceSubRequest
from .v1beta1_device_toleration import V1beta1DeviceToleration
from pydantic import BeforeValidator

__all__ = ("V1beta1DeviceRequest",)


class V1beta1DeviceRequest(BaseModel):
    """DeviceRequest is a request for devices required for a claim. This is typically a request for a single resource like a device, but can also ask for several identical devices."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.resource.v1beta1.DeviceRequest"

    admin_access: Annotated[
        bool | None,
        Field(
            alias="adminAccess",
            description="""AdminAccess indicates that this is a claim for administrative access to the device(s). Claims with AdminAccess are expected to be used for monitoring or other management services for a device.  They ignore all ordinary claims to the device with respect to access modes and any resource allocations.

This field can only be set when deviceClassName is set and no subrequests are specified in the firstAvailable list.

This is an alpha field and requires enabling the DRAAdminAccess feature gate. Admin access is disabled if this field is unset or set to false, otherwise it is enabled.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    allocation_mode: Annotated[
        str | None,
        Field(
            alias="allocationMode",
            description="""AllocationMode and its related fields define how devices are allocated to satisfy this request. Supported values are:

- ExactCount: This request is for a specific number of devices.
  This is the default. The exact number is provided in the
  count field.

- All: This request is for all of the matching devices in a pool.
  At least one device must exist on the node for the allocation to succeed.
  Allocation will fail if some devices are already allocated,
  unless adminAccess is requested.

If AllocationMode is not specified, the default mode is ExactCount. If the mode is ExactCount and count is not specified, the default count is one. Any other requests must specify this field.

This field can only be set when deviceClassName is set and no subrequests are specified in the firstAvailable list.

More modes may get added in the future. Clients must refuse to handle requests with unknown modes.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    capacity: Annotated[
        V1beta1CapacityRequirements,
        Field(
            description="""Capacity define resource requirements against each capacity.

If this field is unset and the device supports multiple allocations, the default value will be applied to each capacity according to requestPolicy. For the capacity that has no requestPolicy, default is the full capacity value.

Applies to each device allocation. If Count > 1, the request fails if there aren't enough devices that meet the requirements. If AllocationMode is set to All, the request fails if there are devices that otherwise match the request, and have this capacity, with a value >= the requested amount, but which cannot be allocated to this request.""",
            exclude_if=lambda v: not v.__pydantic_fields_set__,
        ),
        BeforeValidator(_default_if_none(V1beta1CapacityRequirements)),
    ] = V1beta1CapacityRequirements()

    count: Annotated[
        int | None,
        Field(
            description="""Count is used only when the count mode is "ExactCount". Must be greater than zero. If AllocationMode is ExactCount and this field is not specified, the default is one.

This field can only be set when deviceClassName is set and no subrequests are specified in the firstAvailable list.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    device_class_name: Annotated[
        str | None,
        Field(
            alias="deviceClassName",
            description="""DeviceClassName references a specific DeviceClass, which can define additional configuration and selectors to be inherited by this request.

A class is required if no subrequests are specified in the firstAvailable list and no class can be set if subrequests are specified in the firstAvailable list. Which classes are available depends on the cluster.

Administrators may use this to restrict which devices may get requested by only installing classes with selectors for permitted devices. If users are free to request anything without restrictions, then administrators can create an empty DeviceClass for users to reference.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    first_available: Annotated[
        list[V1beta1DeviceSubRequest],
        Field(
            alias="firstAvailable",
            description="""FirstAvailable contains subrequests, of which exactly one will be satisfied by the scheduler to satisfy this request. It tries to satisfy them in the order in which they are listed here. So if there are two entries in the list, the scheduler will only check the second one if it determines that the first one cannot be used.

This field may only be set in the entries of DeviceClaim.Requests.

DRA does not yet implement scoring, so the scheduler will select the first set of devices that satisfies all the requests in the claim. And if the requirements can be satisfied on more than one node, other scheduling features will determine which node is chosen. This means that the set of devices allocated to a claim might not be the optimal set available to the cluster. Scoring will be implemented later.""",
            exclude_if=lambda v: v == [],
        ),
        BeforeValidator(_collection_if_none("[]")),
    ] = []

    name: Annotated[
        str,
        Field(
            description="""Name can be used to reference this request in a pod.spec.containers[].resources.claims entry and in a constraint of the claim.

Must be a DNS label and unique among all DeviceRequests in a ResourceClaim."""
        ),
    ]

    selectors: Annotated[
        list[V1beta1DeviceSelector],
        Field(
            description="""Selectors define criteria which must be satisfied by a specific device in order for that device to be considered for this request. All selectors must be satisfied for a device to be considered.

This field can only be set when deviceClassName is set and no subrequests are specified in the firstAvailable list.""",
            exclude_if=lambda v: v == [],
        ),
        BeforeValidator(_collection_if_none("[]")),
    ] = []

    tolerations: Annotated[
        list[V1beta1DeviceToleration],
        Field(
            description="""If specified, the request's tolerations.

Tolerations for NoSchedule are required to allocate a device which has a taint with that effect. The same applies to NoExecute.

In addition, should any of the allocated devices get tainted with NoExecute after allocation and that effect is not tolerated, then all pods consuming the ResourceClaim get deleted to evict them. The scheduler will not let new pods reserve the claim while it has these tainted devices. Once all pods are evicted, the claim will get deallocated.

The maximum number of tolerations is 16.

This field can only be set when deviceClassName is set and no subrequests are specified in the firstAvailable list.

This is an alpha field and requires enabling the DRADeviceTaints feature gate.""",
            exclude_if=lambda v: v == [],
        ),
        BeforeValidator(_collection_if_none("[]")),
    ] = []
