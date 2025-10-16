from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_container_status import V1ContainerStatus
from .v1_host_ip import V1HostIP
from .v1_pod_condition import V1PodCondition
from .v1_pod_extended_resource_claim_status import V1PodExtendedResourceClaimStatus
from .v1_pod_ip import V1PodIP
from .v1_pod_resource_claim_status import V1PodResourceClaimStatus
from datetime import datetime

__all__ = ("V1PodStatus",)


class V1PodStatus(BaseModel):
    conditions: list[V1PodCondition] = Field(
        default_factory=lambda: [], alias="conditions"
    )

    container_statuses: list[V1ContainerStatus] = Field(
        default_factory=lambda: [], alias="containerStatuses"
    )

    ephemeral_container_statuses: list[V1ContainerStatus] = Field(
        default_factory=lambda: [], alias="ephemeralContainerStatuses"
    )

    extended_resource_claim_status: V1PodExtendedResourceClaimStatus = Field(
        default_factory=lambda: V1PodExtendedResourceClaimStatus(),
        alias="extendedResourceClaimStatus",
    )

    host_ip: str | None = Field(default_factory=lambda: None, alias="hostIP")

    host_i_ps: list[V1HostIP] = Field(default_factory=lambda: [], alias="hostIPs")

    init_container_statuses: list[V1ContainerStatus] = Field(
        default_factory=lambda: [], alias="initContainerStatuses"
    )

    message: str | None = Field(default_factory=lambda: None, alias="message")

    nominated_node_name: str | None = Field(
        default_factory=lambda: None, alias="nominatedNodeName"
    )

    observed_generation: int | None = Field(
        default_factory=lambda: None, alias="observedGeneration"
    )

    phase: str | None = Field(default_factory=lambda: None, alias="phase")

    pod_ip: str | None = Field(default_factory=lambda: None, alias="podIP")

    pod_i_ps: list[V1PodIP] = Field(default_factory=lambda: [], alias="podIPs")

    qos_class: str | None = Field(default_factory=lambda: None, alias="qosClass")

    reason: str | None = Field(default_factory=lambda: None, alias="reason")

    resize: str | None = Field(default_factory=lambda: None, alias="resize")

    resource_claim_statuses: list[V1PodResourceClaimStatus] = Field(
        default_factory=lambda: [], alias="resourceClaimStatuses"
    )

    start_time: datetime | None = Field(default_factory=lambda: None, alias="startTime")
