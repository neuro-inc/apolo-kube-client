from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from .utils import _collection_if_none
from .utils import _default_if_none
from .v1_volume_node_resources import V1VolumeNodeResources
from pydantic import BeforeValidator

__all__ = ("V1CSINodeDriver",)


class V1CSINodeDriver(BaseModel):
    """CSINodeDriver holds information about the specification of one CSI driver installed on a node"""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.storage.v1.CSINodeDriver"

    allocatable: Annotated[
        V1VolumeNodeResources,
        Field(
            description="""allocatable represents the volume resources of a node that are available for scheduling. This field is beta.""",
            exclude_if=lambda v: not v.__pydantic_fields_set__,
        ),
        BeforeValidator(_default_if_none(V1VolumeNodeResources)),
    ] = V1VolumeNodeResources()

    name: Annotated[
        str,
        Field(
            description="""name represents the name of the CSI driver that this object refers to. This MUST be the same name returned by the CSI GetPluginName() call for that driver."""
        ),
    ]

    node_id: Annotated[
        str,
        Field(
            alias="nodeID",
            description="""nodeID of the node from the driver point of view. This field enables Kubernetes to communicate with storage systems that do not share the same nomenclature for nodes. For example, Kubernetes may refer to a given node as "node1", but the storage system may refer to the same node as "nodeA". When Kubernetes issues a command to the storage system to attach a volume to a specific node, it can use this field to refer to the node name using the ID that the storage system will understand, e.g. "nodeA" instead of "node1". This field is required.""",
        ),
    ]

    topology_keys: Annotated[
        list[str],
        Field(
            alias="topologyKeys",
            description="""topologyKeys is the list of keys supported by the driver. When a driver is initialized on a cluster, it provides a set of topology keys that it understands (e.g. "company.com/zone", "company.com/region"). When a driver is initialized on a node, it provides the same topology keys along with values. Kubelet will expose these topology keys as labels on its own node object. When Kubernetes does topology aware provisioning, it can use this list to determine which labels it should retrieve from the node object and pass back to the driver. It is possible for different nodes to use different topology keys. This can be empty if driver does not support topology.""",
            exclude_if=lambda v: v == [],
        ),
        BeforeValidator(_collection_if_none("[]")),
    ] = []
