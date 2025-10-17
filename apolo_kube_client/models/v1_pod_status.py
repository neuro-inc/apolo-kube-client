from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field
from .v1_container_status import V1ContainerStatus
from .v1_host_ip import V1HostIP
from .v1_pod_condition import V1PodCondition
from .v1_pod_extended_resource_claim_status import V1PodExtendedResourceClaimStatus
from .v1_pod_ip import V1PodIP
from .v1_pod_resource_claim_status import V1PodResourceClaimStatus
from datetime import datetime

__all__ = ("V1PodStatus",)


class V1PodStatus(BaseModel):
    conditions: list[V1PodCondition] = Field(default=[])

    container_statuses: list[V1ContainerStatus] = Field(
        default=[],
        serialization_alias="containerStatuses",
        validation_alias=AliasChoices("container_statuses", "containerStatuses"),
    )

    ephemeral_container_statuses: list[V1ContainerStatus] = Field(
        default=[],
        serialization_alias="ephemeralContainerStatuses",
        validation_alias=AliasChoices(
            "ephemeral_container_statuses", "ephemeralContainerStatuses"
        ),
    )

    extended_resource_claim_status: V1PodExtendedResourceClaimStatus = Field(
        default_factory=lambda: V1PodExtendedResourceClaimStatus(),
        serialization_alias="extendedResourceClaimStatus",
        validation_alias=AliasChoices(
            "extended_resource_claim_status", "extendedResourceClaimStatus"
        ),
    )

    host_ip: str | None = Field(
        default=None,
        serialization_alias="hostIP",
        validation_alias=AliasChoices("host_ip", "hostIP"),
    )

    host_i_ps: list[V1HostIP] = Field(
        default=[],
        serialization_alias="hostIPs",
        validation_alias=AliasChoices("host_i_ps", "hostIPs"),
    )

    init_container_statuses: list[V1ContainerStatus] = Field(
        default=[],
        serialization_alias="initContainerStatuses",
        validation_alias=AliasChoices(
            "init_container_statuses", "initContainerStatuses"
        ),
    )

    message: str | None = Field(default=None)

    nominated_node_name: str | None = Field(
        default=None,
        serialization_alias="nominatedNodeName",
        validation_alias=AliasChoices("nominated_node_name", "nominatedNodeName"),
    )

    observed_generation: int | None = Field(
        default=None,
        serialization_alias="observedGeneration",
        validation_alias=AliasChoices("observed_generation", "observedGeneration"),
    )

    phase: str | None = Field(default=None)

    pod_ip: str | None = Field(
        default=None,
        serialization_alias="podIP",
        validation_alias=AliasChoices("pod_ip", "podIP"),
    )

    pod_i_ps: list[V1PodIP] = Field(
        default=[],
        serialization_alias="podIPs",
        validation_alias=AliasChoices("pod_i_ps", "podIPs"),
    )

    qos_class: str | None = Field(
        default=None,
        serialization_alias="qosClass",
        validation_alias=AliasChoices("qos_class", "qosClass"),
    )

    reason: str | None = Field(default=None)

    resize: str | None = Field(default=None)

    resource_claim_statuses: list[V1PodResourceClaimStatus] = Field(
        default=[],
        serialization_alias="resourceClaimStatuses",
        validation_alias=AliasChoices(
            "resource_claim_statuses", "resourceClaimStatuses"
        ),
    )

    start_time: datetime | None = Field(
        default=None,
        serialization_alias="startTime",
        validation_alias=AliasChoices("start_time", "startTime"),
    )
