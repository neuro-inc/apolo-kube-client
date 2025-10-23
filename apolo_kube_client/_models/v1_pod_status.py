from pydantic import AliasChoices, BaseModel, Field
from .utils import _collection_if_none
from .utils import _default_if_none
from .utils import _exclude_if
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
    ] = Field(default=[], exclude_if=_exclude_if)

    container_statuses: Annotated[
        list[V1ContainerStatus], BeforeValidator(_collection_if_none("[]"))
    ] = Field(
        default=[],
        serialization_alias="containerStatuses",
        validation_alias=AliasChoices("container_statuses", "containerStatuses"),
        exclude_if=_exclude_if,
    )

    ephemeral_container_statuses: Annotated[
        list[V1ContainerStatus], BeforeValidator(_collection_if_none("[]"))
    ] = Field(
        default=[],
        serialization_alias="ephemeralContainerStatuses",
        validation_alias=AliasChoices(
            "ephemeral_container_statuses", "ephemeralContainerStatuses"
        ),
        exclude_if=_exclude_if,
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
        exclude_if=_exclude_if,
    )

    host_ip: str | None = Field(
        default=None,
        serialization_alias="hostIP",
        validation_alias=AliasChoices("host_ip", "hostIP"),
        exclude_if=_exclude_if,
    )

    host_i_ps: Annotated[list[V1HostIP], BeforeValidator(_collection_if_none("[]"))] = (
        Field(
            default=[],
            serialization_alias="hostIPs",
            validation_alias=AliasChoices("host_i_ps", "hostIPs"),
            exclude_if=_exclude_if,
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
        exclude_if=_exclude_if,
    )

    message: str | None = Field(default=None, exclude_if=_exclude_if)

    nominated_node_name: str | None = Field(
        default=None,
        serialization_alias="nominatedNodeName",
        validation_alias=AliasChoices("nominated_node_name", "nominatedNodeName"),
        exclude_if=_exclude_if,
    )

    observed_generation: int | None = Field(
        default=None,
        serialization_alias="observedGeneration",
        validation_alias=AliasChoices("observed_generation", "observedGeneration"),
        exclude_if=_exclude_if,
    )

    phase: str | None = Field(default=None, exclude_if=_exclude_if)

    pod_ip: str | None = Field(
        default=None,
        serialization_alias="podIP",
        validation_alias=AliasChoices("pod_ip", "podIP"),
        exclude_if=_exclude_if,
    )

    pod_i_ps: Annotated[list[V1PodIP], BeforeValidator(_collection_if_none("[]"))] = (
        Field(
            default=[],
            serialization_alias="podIPs",
            validation_alias=AliasChoices("pod_i_ps", "podIPs"),
            exclude_if=_exclude_if,
        )
    )

    qos_class: str | None = Field(
        default=None,
        serialization_alias="qosClass",
        validation_alias=AliasChoices("qos_class", "qosClass"),
        exclude_if=_exclude_if,
    )

    reason: str | None = Field(default=None, exclude_if=_exclude_if)

    resize: str | None = Field(default=None, exclude_if=_exclude_if)

    resource_claim_statuses: Annotated[
        list[V1PodResourceClaimStatus], BeforeValidator(_collection_if_none("[]"))
    ] = Field(
        default=[],
        serialization_alias="resourceClaimStatuses",
        validation_alias=AliasChoices(
            "resource_claim_statuses", "resourceClaimStatuses"
        ),
        exclude_if=_exclude_if,
    )

    start_time: datetime | None = Field(
        default=None,
        serialization_alias="startTime",
        validation_alias=AliasChoices("start_time", "startTime"),
        exclude_if=_exclude_if,
    )
