from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from .utils import _collection_if_none
from .v1_device_attribute import V1DeviceAttribute
from .v1_device_capacity import V1DeviceCapacity
from .v1_device_counter_consumption import V1DeviceCounterConsumption
from .v1_device_taint import V1DeviceTaint
from .v1_node_selector import V1NodeSelector
from pydantic import BeforeValidator

__all__ = ("V1Device",)


class V1Device(BaseModel):
    """Device represents one individual hardware instance that can be selected based on its attributes. Besides the name, exactly one field must be set."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.resource.v1.Device"

    all_nodes: Annotated[
        bool | None,
        Field(
            alias="allNodes",
            description="""AllNodes indicates that all nodes have access to the device.

Must only be set if Spec.PerDeviceNodeSelection is set to true. At most one of NodeName, NodeSelector and AllNodes can be set.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    allow_multiple_allocations: Annotated[
        bool | None,
        Field(
            alias="allowMultipleAllocations",
            description="""AllowMultipleAllocations marks whether the device is allowed to be allocated to multiple DeviceRequests.

If AllowMultipleAllocations is set to true, the device can be allocated more than once, and all of its capacity is consumable, regardless of whether the requestPolicy is defined or not.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    attributes: Annotated[
        dict[str, V1DeviceAttribute],
        Field(
            description="""Attributes defines the set of attributes for this device. The name of each attribute must be unique in that set.

The maximum number of attributes and capacities combined is 32.""",
            exclude_if=lambda v: v == {},
        ),
        BeforeValidator(_collection_if_none("{}")),
    ] = {}

    binding_conditions: Annotated[
        list[str],
        Field(
            alias="bindingConditions",
            description="""BindingConditions defines the conditions for proceeding with binding. All of these conditions must be set in the per-device status conditions with a value of True to proceed with binding the pod to the node while scheduling the pod.

The maximum number of binding conditions is 4.

The conditions must be a valid condition type string.

This is an alpha field and requires enabling the DRADeviceBindingConditions and DRAResourceClaimDeviceStatus feature gates.""",
            exclude_if=lambda v: v == [],
        ),
        BeforeValidator(_collection_if_none("[]")),
    ] = []

    binding_failure_conditions: Annotated[
        list[str],
        Field(
            alias="bindingFailureConditions",
            description="""BindingFailureConditions defines the conditions for binding failure. They may be set in the per-device status conditions. If any is set to "True", a binding failure occurred.

The maximum number of binding failure conditions is 4.

The conditions must be a valid condition type string.

This is an alpha field and requires enabling the DRADeviceBindingConditions and DRAResourceClaimDeviceStatus feature gates.""",
            exclude_if=lambda v: v == [],
        ),
        BeforeValidator(_collection_if_none("[]")),
    ] = []

    binds_to_node: Annotated[
        bool | None,
        Field(
            alias="bindsToNode",
            description="""BindsToNode indicates if the usage of an allocation involving this device has to be limited to exactly the node that was chosen when allocating the claim. If set to true, the scheduler will set the ResourceClaim.Status.Allocation.NodeSelector to match the node where the allocation was made.

This is an alpha field and requires enabling the DRADeviceBindingConditions and DRAResourceClaimDeviceStatus feature gates.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    capacity: Annotated[
        dict[str, V1DeviceCapacity],
        Field(
            description="""Capacity defines the set of capacities for this device. The name of each capacity must be unique in that set.

The maximum number of attributes and capacities combined is 32.""",
            exclude_if=lambda v: v == {},
        ),
        BeforeValidator(_collection_if_none("{}")),
    ] = {}

    consumes_counters: Annotated[
        list[V1DeviceCounterConsumption],
        Field(
            alias="consumesCounters",
            description="""ConsumesCounters defines a list of references to sharedCounters and the set of counters that the device will consume from those counter sets.

There can only be a single entry per counterSet.

The total number of device counter consumption entries must be <= 32. In addition, the total number in the entire ResourceSlice must be <= 1024 (for example, 64 devices with 16 counters each).""",
            exclude_if=lambda v: v == [],
        ),
        BeforeValidator(_collection_if_none("[]")),
    ] = []

    name: Annotated[
        str,
        Field(
            description="""Name is unique identifier among all devices managed by the driver in the pool. It must be a DNS label."""
        ),
    ]

    node_name: Annotated[
        str | None,
        Field(
            alias="nodeName",
            description="""NodeName identifies the node where the device is available.

Must only be set if Spec.PerDeviceNodeSelection is set to true. At most one of NodeName, NodeSelector and AllNodes can be set.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    node_selector: Annotated[
        V1NodeSelector | None,
        Field(
            alias="nodeSelector",
            description="""NodeSelector defines the nodes where the device is available.

Must use exactly one term.

Must only be set if Spec.PerDeviceNodeSelection is set to true. At most one of NodeName, NodeSelector and AllNodes can be set.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    taints: Annotated[
        list[V1DeviceTaint],
        Field(
            description="""If specified, these are the driver-defined taints.

The maximum number of taints is 4.

This is an alpha field and requires enabling the DRADeviceTaints feature gate.""",
            exclude_if=lambda v: v == [],
        ),
        BeforeValidator(_collection_if_none("[]")),
    ] = []
