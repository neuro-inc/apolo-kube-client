from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_service_port import V1ServicePort
from .v1_session_affinity_config import V1SessionAffinityConfig

__all__ = ("V1ServiceSpec",)


class V1ServiceSpec(BaseModel):
    allocate_load_balancer_node_ports: bool | None = Field(
        default_factory=lambda: None, alias="allocateLoadBalancerNodePorts"
    )

    cluster_ip: str | None = Field(default_factory=lambda: None, alias="clusterIP")

    cluster_i_ps: list[str] = Field(default_factory=lambda: [], alias="clusterIPs")

    external_i_ps: list[str] = Field(default_factory=lambda: [], alias="externalIPs")

    external_name: str | None = Field(
        default_factory=lambda: None, alias="externalName"
    )

    external_traffic_policy: str | None = Field(
        default_factory=lambda: None, alias="externalTrafficPolicy"
    )

    health_check_node_port: int | None = Field(
        default_factory=lambda: None, alias="healthCheckNodePort"
    )

    internal_traffic_policy: str | None = Field(
        default_factory=lambda: None, alias="internalTrafficPolicy"
    )

    ip_families: list[str] = Field(default_factory=lambda: [], alias="ipFamilies")

    ip_family_policy: str | None = Field(
        default_factory=lambda: None, alias="ipFamilyPolicy"
    )

    load_balancer_class: str | None = Field(
        default_factory=lambda: None, alias="loadBalancerClass"
    )

    load_balancer_ip: str | None = Field(
        default_factory=lambda: None, alias="loadBalancerIP"
    )

    load_balancer_source_ranges: list[str] = Field(
        default_factory=lambda: [], alias="loadBalancerSourceRanges"
    )

    ports: list[V1ServicePort] = Field(default_factory=lambda: [], alias="ports")

    publish_not_ready_addresses: bool | None = Field(
        default_factory=lambda: None, alias="publishNotReadyAddresses"
    )

    selector: dict[str, str] = Field(default_factory=lambda: {}, alias="selector")

    session_affinity: str | None = Field(
        default_factory=lambda: None, alias="sessionAffinity"
    )

    session_affinity_config: V1SessionAffinityConfig = Field(
        default_factory=lambda: V1SessionAffinityConfig(), alias="sessionAffinityConfig"
    )

    traffic_distribution: str | None = Field(
        default_factory=lambda: None, alias="trafficDistribution"
    )

    type: str | None = Field(default_factory=lambda: None, alias="type")
