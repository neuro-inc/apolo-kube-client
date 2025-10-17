from pydantic import AliasChoices, BaseModel, Field
from .v1_service_port import V1ServicePort
from .v1_session_affinity_config import V1SessionAffinityConfig

__all__ = ("V1ServiceSpec",)


class V1ServiceSpec(BaseModel):
    allocate_load_balancer_node_ports: bool | None = Field(
        default=None,
        serialization_alias="allocateLoadBalancerNodePorts",
        validation_alias=AliasChoices(
            "allocate_load_balancer_node_ports", "allocateLoadBalancerNodePorts"
        ),
    )

    cluster_ip: str | None = Field(
        default=None,
        serialization_alias="clusterIP",
        validation_alias=AliasChoices("cluster_ip", "clusterIP"),
    )

    cluster_i_ps: list[str] = Field(
        default=[],
        serialization_alias="clusterIPs",
        validation_alias=AliasChoices("cluster_i_ps", "clusterIPs"),
    )

    external_i_ps: list[str] = Field(
        default=[],
        serialization_alias="externalIPs",
        validation_alias=AliasChoices("external_i_ps", "externalIPs"),
    )

    external_name: str | None = Field(
        default=None,
        serialization_alias="externalName",
        validation_alias=AliasChoices("external_name", "externalName"),
    )

    external_traffic_policy: str | None = Field(
        default=None,
        serialization_alias="externalTrafficPolicy",
        validation_alias=AliasChoices(
            "external_traffic_policy", "externalTrafficPolicy"
        ),
    )

    health_check_node_port: int | None = Field(
        default=None,
        serialization_alias="healthCheckNodePort",
        validation_alias=AliasChoices("health_check_node_port", "healthCheckNodePort"),
    )

    internal_traffic_policy: str | None = Field(
        default=None,
        serialization_alias="internalTrafficPolicy",
        validation_alias=AliasChoices(
            "internal_traffic_policy", "internalTrafficPolicy"
        ),
    )

    ip_families: list[str] = Field(
        default=[],
        serialization_alias="ipFamilies",
        validation_alias=AliasChoices("ip_families", "ipFamilies"),
    )

    ip_family_policy: str | None = Field(
        default=None,
        serialization_alias="ipFamilyPolicy",
        validation_alias=AliasChoices("ip_family_policy", "ipFamilyPolicy"),
    )

    load_balancer_class: str | None = Field(
        default=None,
        serialization_alias="loadBalancerClass",
        validation_alias=AliasChoices("load_balancer_class", "loadBalancerClass"),
    )

    load_balancer_ip: str | None = Field(
        default=None,
        serialization_alias="loadBalancerIP",
        validation_alias=AliasChoices("load_balancer_ip", "loadBalancerIP"),
    )

    load_balancer_source_ranges: list[str] = Field(
        default=[],
        serialization_alias="loadBalancerSourceRanges",
        validation_alias=AliasChoices(
            "load_balancer_source_ranges", "loadBalancerSourceRanges"
        ),
    )

    ports: list[V1ServicePort] = []

    publish_not_ready_addresses: bool | None = Field(
        default=None,
        serialization_alias="publishNotReadyAddresses",
        validation_alias=AliasChoices(
            "publish_not_ready_addresses", "publishNotReadyAddresses"
        ),
    )

    selector: dict[str, str] = {}

    session_affinity: str | None = Field(
        default=None,
        serialization_alias="sessionAffinity",
        validation_alias=AliasChoices("session_affinity", "sessionAffinity"),
    )

    session_affinity_config: V1SessionAffinityConfig = Field(
        default_factory=lambda: V1SessionAffinityConfig(),
        serialization_alias="sessionAffinityConfig",
        validation_alias=AliasChoices(
            "session_affinity_config", "sessionAffinityConfig"
        ),
    )

    traffic_distribution: str | None = Field(
        default=None,
        serialization_alias="trafficDistribution",
        validation_alias=AliasChoices("traffic_distribution", "trafficDistribution"),
    )

    type: str | None = None
