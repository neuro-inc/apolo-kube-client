from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from .utils import _collection_if_none
from .v1beta1_device_toleration import V1beta1DeviceToleration
from pydantic import BeforeValidator

__all__ = ("V1beta1DeviceRequestAllocationResult",)


class V1beta1DeviceRequestAllocationResult(BaseModel):
    """DeviceRequestAllocationResult contains the allocation result for one request."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = (
        "io.k8s.api.resource.v1beta1.DeviceRequestAllocationResult"
    )

    admin_access: Annotated[
        bool | None,
        Field(
            alias="adminAccess",
            description="""AdminAccess indicates that this device was allocated for administrative access. See the corresponding request field for a definition of mode.

This is an alpha field and requires enabling the DRAAdminAccess feature gate. Admin access is disabled if this field is unset or set to false, otherwise it is enabled.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    binding_conditions: Annotated[
        list[str],
        Field(
            alias="bindingConditions",
            description="""BindingConditions contains a copy of the BindingConditions from the corresponding ResourceSlice at the time of allocation.

This is an alpha field and requires enabling the DRADeviceBindingConditions and DRAResourceClaimDeviceStatus feature gates.""",
            exclude_if=lambda v: v == [],
        ),
        BeforeValidator(_collection_if_none("[]")),
    ] = []

    binding_failure_conditions: Annotated[
        list[str],
        Field(
            alias="bindingFailureConditions",
            description="""BindingFailureConditions contains a copy of the BindingFailureConditions from the corresponding ResourceSlice at the time of allocation.

This is an alpha field and requires enabling the DRADeviceBindingConditions and DRAResourceClaimDeviceStatus feature gates.""",
            exclude_if=lambda v: v == [],
        ),
        BeforeValidator(_collection_if_none("[]")),
    ] = []

    consumed_capacity: Annotated[
        dict[str, str],
        Field(
            alias="consumedCapacity",
            description="""ConsumedCapacity tracks the amount of capacity consumed per device as part of the claim request. The consumed amount may differ from the requested amount: it is rounded up to the nearest valid value based on the device’s requestPolicy if applicable (i.e., may not be less than the requested amount).

The total consumed capacity for each device must not exceed the DeviceCapacity's Value.

This field is populated only for devices that allow multiple allocations. All capacity entries are included, even if the consumed amount is zero.""",
            exclude_if=lambda v: v == {},
        ),
        BeforeValidator(_collection_if_none("{}")),
    ] = {}

    device: Annotated[
        str,
        Field(
            description="""Device references one device instance via its name in the driver's resource pool. It must be a DNS label."""
        ),
    ]

    driver: Annotated[
        str,
        Field(
            description="""Driver specifies the name of the DRA driver whose kubelet plugin should be invoked to process the allocation once the claim is needed on a node.

Must be a DNS subdomain and should end with a DNS domain owned by the vendor of the driver."""
        ),
    ]

    pool: Annotated[
        str,
        Field(
            description="""This name together with the driver name and the device name field identify which device was allocated (`<driver name>/<pool name>/<device name>`).

Must not be longer than 253 characters and may contain one or more DNS sub-domains separated by slashes."""
        ),
    ]

    request: Annotated[
        str,
        Field(
            description="""Request is the name of the request in the claim which caused this device to be allocated. If it references a subrequest in the firstAvailable list on a DeviceRequest, this field must include both the name of the main request and the subrequest using the format <main request>/<subrequest>.

Multiple devices may have been allocated per request."""
        ),
    ]

    share_id: Annotated[
        str | None,
        Field(
            alias="shareID",
            description="""ShareID uniquely identifies an individual allocation share of the device, used when the device supports multiple simultaneous allocations. It serves as an additional map key to differentiate concurrent shares of the same device.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    tolerations: Annotated[
        list[V1beta1DeviceToleration],
        Field(
            description="""A copy of all tolerations specified in the request at the time when the device got allocated.

The maximum number of tolerations is 16.

This is an alpha field and requires enabling the DRADeviceTaints feature gate.""",
            exclude_if=lambda v: v == [],
        ),
        BeforeValidator(_collection_if_none("[]")),
    ] = []
