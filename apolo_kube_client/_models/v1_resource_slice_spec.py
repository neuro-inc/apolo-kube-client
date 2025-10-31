from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from .utils import _collection_if_none
from .v1_counter_set import V1CounterSet
from .v1_device import V1Device
from .v1_node_selector import V1NodeSelector
from .v1_resource_pool import V1ResourcePool
from pydantic import BeforeValidator

__all__ = ("V1ResourceSliceSpec",)


class V1ResourceSliceSpec(BaseModel):
    """ResourceSliceSpec contains the information published by the driver in one ResourceSlice."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.resource.v1.ResourceSliceSpec"

    all_nodes: Annotated[
        bool | None,
        Field(
            alias="allNodes",
            description="""AllNodes indicates that all nodes have access to the resources in the pool.

Exactly one of NodeName, NodeSelector, AllNodes, and PerDeviceNodeSelection must be set.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    devices: Annotated[
        list[V1Device],
        Field(
            description="""Devices lists some or all of the devices in this pool.

Must not have more than 128 entries.""",
            exclude_if=lambda v: v == [],
        ),
        BeforeValidator(_collection_if_none("[]")),
    ] = []

    driver: Annotated[
        str,
        Field(
            description="""Driver identifies the DRA driver providing the capacity information. A field selector can be used to list only ResourceSlice objects with a certain driver name.

Must be a DNS subdomain and should end with a DNS domain owned by the vendor of the driver. This field is immutable."""
        ),
    ]

    node_name: Annotated[
        str | None,
        Field(
            alias="nodeName",
            description="""NodeName identifies the node which provides the resources in this pool. A field selector can be used to list only ResourceSlice objects belonging to a certain node.

This field can be used to limit access from nodes to ResourceSlices with the same node name. It also indicates to autoscalers that adding new nodes of the same type as some old node might also make new resources available.

Exactly one of NodeName, NodeSelector, AllNodes, and PerDeviceNodeSelection must be set. This field is immutable.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    node_selector: Annotated[
        V1NodeSelector | None,
        Field(
            alias="nodeSelector",
            description="""NodeSelector defines which nodes have access to the resources in the pool, when that pool is not limited to a single node.

Must use exactly one term.

Exactly one of NodeName, NodeSelector, AllNodes, and PerDeviceNodeSelection must be set.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    per_device_node_selection: Annotated[
        bool | None,
        Field(
            alias="perDeviceNodeSelection",
            description="""PerDeviceNodeSelection defines whether the access from nodes to resources in the pool is set on the ResourceSlice level or on each device. If it is set to true, every device defined the ResourceSlice must specify this individually.

Exactly one of NodeName, NodeSelector, AllNodes, and PerDeviceNodeSelection must be set.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    pool: Annotated[
        V1ResourcePool,
        Field(
            description="""Pool describes the pool that this ResourceSlice belongs to."""
        ),
    ]

    shared_counters: Annotated[
        list[V1CounterSet],
        Field(
            alias="sharedCounters",
            description="""SharedCounters defines a list of counter sets, each of which has a name and a list of counters available.

The names of the SharedCounters must be unique in the ResourceSlice.

The maximum number of counters in all sets is 32.""",
            exclude_if=lambda v: v == [],
        ),
        BeforeValidator(_collection_if_none("[]")),
    ] = []
