from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from .utils import _collection_if_none
from .utils import _default_if_none
from .v1_attached_volume import V1AttachedVolume
from .v1_container_image import V1ContainerImage
from .v1_node_address import V1NodeAddress
from .v1_node_condition import V1NodeCondition
from .v1_node_config_status import V1NodeConfigStatus
from .v1_node_daemon_endpoints import V1NodeDaemonEndpoints
from .v1_node_features import V1NodeFeatures
from .v1_node_runtime_handler import V1NodeRuntimeHandler
from .v1_node_system_info import V1NodeSystemInfo
from pydantic import BeforeValidator

__all__ = ("V1NodeStatus",)


class V1NodeStatus(BaseModel):
    """NodeStatus is information about the current status of a node."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.core.v1.NodeStatus"

    addresses: Annotated[
        list[V1NodeAddress],
        Field(
            description="""List of addresses reachable to the node. Queried from cloud provider, if available. More info: https://kubernetes.io/docs/reference/node/node-status/#addresses Note: This field is declared as mergeable, but the merge key is not sufficiently unique, which can cause data corruption when it is merged. Callers should instead use a full-replacement patch. See https://pr.k8s.io/79391 for an example. Consumers should assume that addresses can change during the lifetime of a Node. However, there are some exceptions where this may not be possible, such as Pods that inherit a Node's address in its own status or consumers of the downward API (status.hostIP).""",
            exclude_if=lambda v: v == [],
        ),
        BeforeValidator(_collection_if_none("[]")),
    ] = []

    allocatable: Annotated[
        dict[str, str],
        Field(
            description="""Allocatable represents the resources of a node that are available for scheduling. Defaults to Capacity.""",
            exclude_if=lambda v: v == {},
        ),
        BeforeValidator(_collection_if_none("{}")),
    ] = {}

    capacity: Annotated[
        dict[str, str],
        Field(
            description="""Capacity represents the total resources of a node. More info: https://kubernetes.io/docs/reference/node/node-status/#capacity""",
            exclude_if=lambda v: v == {},
        ),
        BeforeValidator(_collection_if_none("{}")),
    ] = {}

    conditions: Annotated[
        list[V1NodeCondition],
        Field(
            description="""Conditions is an array of current observed node conditions. More info: https://kubernetes.io/docs/reference/node/node-status/#condition""",
            exclude_if=lambda v: v == [],
        ),
        BeforeValidator(_collection_if_none("[]")),
    ] = []

    config: Annotated[
        V1NodeConfigStatus,
        Field(
            description="""Status of the config assigned to the node via the dynamic Kubelet config feature.""",
            exclude_if=lambda v: not v.__pydantic_fields_set__,
        ),
        BeforeValidator(_default_if_none(V1NodeConfigStatus)),
    ] = V1NodeConfigStatus()

    daemon_endpoints: Annotated[
        V1NodeDaemonEndpoints,
        Field(
            alias="daemonEndpoints",
            description="""Endpoints of daemons running on the Node.""",
            exclude_if=lambda v: not v.__pydantic_fields_set__,
        ),
        BeforeValidator(_default_if_none(V1NodeDaemonEndpoints)),
    ] = V1NodeDaemonEndpoints()

    features: Annotated[
        V1NodeFeatures,
        Field(
            description="""Features describes the set of features implemented by the CRI implementation.""",
            exclude_if=lambda v: not v.__pydantic_fields_set__,
        ),
        BeforeValidator(_default_if_none(V1NodeFeatures)),
    ] = V1NodeFeatures()

    images: Annotated[
        list[V1ContainerImage],
        Field(
            description="""List of container images on this node""",
            exclude_if=lambda v: v == [],
        ),
        BeforeValidator(_collection_if_none("[]")),
    ] = []

    node_info: Annotated[
        V1NodeSystemInfo | None,
        Field(
            alias="nodeInfo",
            description="""Set of ids/uuids to uniquely identify the node. More info: https://kubernetes.io/docs/reference/node/node-status/#info""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    phase: Annotated[
        str | None,
        Field(
            description="""NodePhase is the recently observed lifecycle phase of the node. More info: https://kubernetes.io/docs/concepts/nodes/node/#phase The field is never populated, and now is deprecated.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    runtime_handlers: Annotated[
        list[V1NodeRuntimeHandler],
        Field(
            alias="runtimeHandlers",
            description="""The available runtime handlers.""",
            exclude_if=lambda v: v == [],
        ),
        BeforeValidator(_collection_if_none("[]")),
    ] = []

    volumes_attached: Annotated[
        list[V1AttachedVolume],
        Field(
            alias="volumesAttached",
            description="""List of volumes that are attached to the node.""",
            exclude_if=lambda v: v == [],
        ),
        BeforeValidator(_collection_if_none("[]")),
    ] = []

    volumes_in_use: Annotated[
        list[str],
        Field(
            alias="volumesInUse",
            description="""List of attachable volumes in use (mounted) by the node.""",
            exclude_if=lambda v: v == [],
        ),
        BeforeValidator(_collection_if_none("[]")),
    ] = []
