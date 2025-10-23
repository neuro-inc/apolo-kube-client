from pydantic import AliasChoices, BaseModel, Field
from .utils import _collection_if_none
from .utils import _default_if_none
from .utils import _exclude_if
from .v1_service_port import V1ServicePort
from .v1_session_affinity_config import V1SessionAffinityConfig
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1ServiceSpec",)


class V1ServiceSpec(BaseModel):
    allocate_load_balancer_node_ports: bool | None = Field(
        default=None,
        serialization_alias="allocateLoadBalancerNodePorts",
        validation_alias=AliasChoices(
            "allocate_load_balancer_node_ports", "allocateLoadBalancerNodePorts"
        ),
        exclude_if=_exclude_if,
    )

    cluster_ip: str | None = Field(
        default=None,
        serialization_alias="clusterIP",
        validation_alias=AliasChoices("cluster_ip", "clusterIP"),
        exclude_if=_exclude_if,
    )

    cluster_i_ps: Annotated[list[str], BeforeValidator(_collection_if_none("[]"))] = (
        Field(
            default=[],
            serialization_alias="clusterIPs",
            validation_alias=AliasChoices("cluster_i_ps", "clusterIPs"),
            exclude_if=_exclude_if,
        )
    )

    external_i_ps: Annotated[list[str], BeforeValidator(_collection_if_none("[]"))] = (
        Field(
            default=[],
            serialization_alias="externalIPs",
            validation_alias=AliasChoices("external_i_ps", "externalIPs"),
            exclude_if=_exclude_if,
        )
    )

    external_name: str | None = Field(
        default=None,
        serialization_alias="externalName",
        validation_alias=AliasChoices("external_name", "externalName"),
        exclude_if=_exclude_if,
    )

    external_traffic_policy: str | None = Field(
        default=None,
        serialization_alias="externalTrafficPolicy",
        validation_alias=AliasChoices(
            "external_traffic_policy", "externalTrafficPolicy"
        ),
        exclude_if=_exclude_if,
    )

    health_check_node_port: int | None = Field(
        default=None,
        serialization_alias="healthCheckNodePort",
        validation_alias=AliasChoices("health_check_node_port", "healthCheckNodePort"),
        exclude_if=_exclude_if,
    )

    internal_traffic_policy: str | None = Field(
        default=None,
        serialization_alias="internalTrafficPolicy",
        validation_alias=AliasChoices(
            "internal_traffic_policy", "internalTrafficPolicy"
        ),
        exclude_if=_exclude_if,
    )

    ip_families: Annotated[list[str], BeforeValidator(_collection_if_none("[]"))] = (
        Field(
            default=[],
            serialization_alias="ipFamilies",
            validation_alias=AliasChoices("ip_families", "ipFamilies"),
            exclude_if=_exclude_if,
        )
    )

    ip_family_policy: str | None = Field(
        default=None,
        serialization_alias="ipFamilyPolicy",
        validation_alias=AliasChoices("ip_family_policy", "ipFamilyPolicy"),
        exclude_if=_exclude_if,
    )

    load_balancer_class: str | None = Field(
        default=None,
        serialization_alias="loadBalancerClass",
        validation_alias=AliasChoices("load_balancer_class", "loadBalancerClass"),
        exclude_if=_exclude_if,
    )

    load_balancer_ip: str | None = Field(
        default=None,
        serialization_alias="loadBalancerIP",
        validation_alias=AliasChoices("load_balancer_ip", "loadBalancerIP"),
        exclude_if=_exclude_if,
    )

    load_balancer_source_ranges: Annotated[
        list[str], BeforeValidator(_collection_if_none("[]"))
    ] = Field(
        default=[],
        serialization_alias="loadBalancerSourceRanges",
        validation_alias=AliasChoices(
            "load_balancer_source_ranges", "loadBalancerSourceRanges"
        ),
        exclude_if=_exclude_if,
    )

    ports: Annotated[
        list[V1ServicePort], BeforeValidator(_collection_if_none("[]"))
    ] = Field(default=[], exclude_if=_exclude_if)

    publish_not_ready_addresses: bool | None = Field(
        default=None,
        serialization_alias="publishNotReadyAddresses",
        validation_alias=AliasChoices(
            "publish_not_ready_addresses", "publishNotReadyAddresses"
        ),
        exclude_if=_exclude_if,
    )

    selector: Annotated[dict[str, str], BeforeValidator(_collection_if_none("{}"))] = (
        Field(default={}, exclude_if=_exclude_if)
    )

    session_affinity: str | None = Field(
        default=None,
        serialization_alias="sessionAffinity",
        validation_alias=AliasChoices("session_affinity", "sessionAffinity"),
        exclude_if=_exclude_if,
    )

    session_affinity_config: Annotated[
        V1SessionAffinityConfig,
        BeforeValidator(_default_if_none(V1SessionAffinityConfig)),
    ] = Field(
        default_factory=lambda: V1SessionAffinityConfig(),
        serialization_alias="sessionAffinityConfig",
        validation_alias=AliasChoices(
            "session_affinity_config", "sessionAffinityConfig"
        ),
        exclude_if=_exclude_if,
    )

    traffic_distribution: str | None = Field(
        default=None,
        serialization_alias="trafficDistribution",
        validation_alias=AliasChoices("traffic_distribution", "trafficDistribution"),
        exclude_if=_exclude_if,
    )

    type: str | None = Field(default=None, exclude_if=_exclude_if)
