from pydantic import BaseModel, Field

from .v1_service_port import V1ServicePort
from .v1_session_affinity_config import V1SessionAffinityConfig


class V1ServiceSpec(BaseModel):
    allocate_load_balancer_node_ports: bool | None = Field(
        None, alias="allocateLoadBalancerNodePorts"
    )

    cluster_ip: str | None = Field(None, alias="clusterIP")

    cluster_i_ps: list[str] | None = Field(None, alias="clusterIPs")

    external_i_ps: list[str] | None = Field(None, alias="externalIPs")

    external_name: str | None = Field(None, alias="externalName")

    external_traffic_policy: str | None = Field(None, alias="externalTrafficPolicy")

    health_check_node_port: int | None = Field(None, alias="healthCheckNodePort")

    internal_traffic_policy: str | None = Field(None, alias="internalTrafficPolicy")

    ip_families: list[str] | None = Field(None, alias="ipFamilies")

    ip_family_policy: str | None = Field(None, alias="ipFamilyPolicy")

    load_balancer_class: str | None = Field(None, alias="loadBalancerClass")

    load_balancer_ip: str | None = Field(None, alias="loadBalancerIP")

    load_balancer_source_ranges: list[str] | None = Field(
        None, alias="loadBalancerSourceRanges"
    )

    ports: list[V1ServicePort] | None = Field(None, alias="ports")

    publish_not_ready_addresses: bool | None = Field(
        None, alias="publishNotReadyAddresses"
    )

    selector: dict(str, str) | None = Field(None, alias="selector")

    session_affinity: str | None = Field(None, alias="sessionAffinity")

    session_affinity_config: V1SessionAffinityConfig | None = Field(
        None, alias="sessionAffinityConfig"
    )

    traffic_distribution: str | None = Field(None, alias="trafficDistribution")

    type: str | None = Field(None, alias="type")
