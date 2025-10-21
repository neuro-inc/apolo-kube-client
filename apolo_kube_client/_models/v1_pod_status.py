from pydantic import AliasChoices, BaseModel, Field
from .utils import _collection_if_none
from .utils import _default_if_none
from .v1_container_status import V1ContainerStatus
from .v1_host_ip import V1HostIP
from .v1_pod_condition import V1PodCondition
from .v1_pod_extended_resource_claim_status import V1PodExtendedResourceClaimStatus
from .v1_pod_ip import V1PodIP
from .v1_pod_resource_claim_status import V1PodResourceClaimStatus
from datetime import datetime
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1PodStatus",)


class V1PodStatus(BaseModel):
    conditions: Annotated[
        list[V1PodCondition], BeforeValidator(_collection_if_none("[]"))
    ] = []

    container_statuses: Annotated[
        list[V1ContainerStatus], BeforeValidator(_collection_if_none("[]"))
    ] = Field(
        default=[],
        serialization_alias="containerStatuses",
        validation_alias=AliasChoices("container_statuses", "containerStatuses"),
    )

    ephemeral_container_statuses: Annotated[
        list[V1ContainerStatus], BeforeValidator(_collection_if_none("[]"))
    ] = Field(
        default=[],
        serialization_alias="ephemeralContainerStatuses",
        validation_alias=AliasChoices(
            "ephemeral_container_statuses", "ephemeralContainerStatuses"
        ),
    )

    extended_resource_claim_status: Annotated[
        V1PodExtendedResourceClaimStatus,
        BeforeValidator(_default_if_none(V1PodExtendedResourceClaimStatus)),
    ] = Field(
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

    host_i_ps: Annotated[list[V1HostIP], BeforeValidator(_collection_if_none("[]"))] = (
        Field(
            default=[],
            serialization_alias="hostIPs",
            validation_alias=AliasChoices("host_i_ps", "hostIPs"),
        )
    )

    init_container_statuses: Annotated[
        list[V1ContainerStatus], BeforeValidator(_collection_if_none("[]"))
    ] = Field(
        default=[],
        serialization_alias="initContainerStatuses",
        validation_alias=AliasChoices(
            "init_container_statuses", "initContainerStatuses"
        ),
    )

    message: str | None = None

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

    phase: str | None = None

    pod_ip: str | None = Field(
        default=None,
        serialization_alias="podIP",
        validation_alias=AliasChoices("pod_ip", "podIP"),
    )

    pod_i_ps: Annotated[list[V1PodIP], BeforeValidator(_collection_if_none("[]"))] = (
        Field(
            default=[],
            serialization_alias="podIPs",
            validation_alias=AliasChoices("pod_i_ps", "podIPs"),
        )
    )

    qos_class: str | None = Field(
        default=None,
        serialization_alias="qosClass",
        validation_alias=AliasChoices("qos_class", "qosClass"),
    )

    reason: str | None = None

    resize: str | None = None

    resource_claim_statuses: Annotated[
        list[V1PodResourceClaimStatus], BeforeValidator(_collection_if_none("[]"))
    ] = Field(
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
