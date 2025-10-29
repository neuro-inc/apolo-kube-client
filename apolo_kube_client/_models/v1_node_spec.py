from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from .utils import _collection_if_none
from .utils import _default_if_none
from .v1_node_config_source import V1NodeConfigSource
from .v1_taint import V1Taint
from pydantic import BeforeValidator

__all__ = ("V1NodeSpec",)


class V1NodeSpec(BaseModel):
    """NodeSpec describes the attributes that a node is created with."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.core.v1.NodeSpec"

    config_source: Annotated[
        V1NodeConfigSource,
        Field(
            alias="configSource",
            description="""Deprecated: Previously used to specify the source of the node's configuration for the DynamicKubeletConfig feature. This feature is removed.""",
            exclude_if=lambda v: not v.__pydantic_fields_set__,
        ),
        BeforeValidator(_default_if_none(V1NodeConfigSource)),
    ] = V1NodeConfigSource()

    external_id: Annotated[
        str | None,
        Field(
            alias="externalID",
            description="""Deprecated. Not all kubelets will set this field. Remove field after 1.13. see: https://issues.k8s.io/61966""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    pod_cidr: Annotated[
        str | None,
        Field(
            alias="podCIDR",
            description="""PodCIDR represents the pod IP range assigned to the node.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    pod_cid_rs: Annotated[
        list[str],
        Field(
            alias="podCIDRs",
            description="""podCIDRs represents the IP ranges assigned to the node for usage by Pods on that node. If this field is specified, the 0th entry must match the podCIDR field. It may contain at most 1 value for each of IPv4 and IPv6.""",
            exclude_if=lambda v: v == [],
        ),
        BeforeValidator(_collection_if_none("[]")),
    ] = []

    provider_id: Annotated[
        str | None,
        Field(
            alias="providerID",
            description="""ID of the node assigned by the cloud provider in the format: <ProviderName>://<ProviderSpecificNodeID>""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    taints: Annotated[
        list[V1Taint],
        Field(
            description="""If specified, the node's taints.""",
            exclude_if=lambda v: v == [],
        ),
        BeforeValidator(_collection_if_none("[]")),
    ] = []

    unschedulable: Annotated[
        bool | None,
        Field(
            description="""Unschedulable controls node schedulability of new pods. By default, node is schedulable. More info: https://kubernetes.io/docs/concepts/nodes/node/#manual-node-administration""",
            exclude_if=lambda v: v is None,
        ),
    ] = None
