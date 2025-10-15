from datetime import datetime

from pydantic import BaseModel, Field

from .v1_container_status import V1ContainerStatus
from .v1_host_i_p import V1HostIP
from .v1_pod_condition import V1PodCondition
from .v1_pod_i_p import V1PodIP
from .v1_pod_resource_claim_status import V1PodResourceClaimStatus


class V1PodStatus(BaseModel):
    conditions: list[V1PodCondition] | None = Field(None, alias="conditions")

    container_statuses: list[V1ContainerStatus] | None = Field(
        None, alias="containerStatuses"
    )

    ephemeral_container_statuses: list[V1ContainerStatus] | None = Field(
        None, alias="ephemeralContainerStatuses"
    )

    host_ip: str | None = Field(None, alias="hostIP")

    host_i_ps: list[V1HostIP] | None = Field(None, alias="hostIPs")

    init_container_statuses: list[V1ContainerStatus] | None = Field(
        None, alias="initContainerStatuses"
    )

    message: str | None = Field(None, alias="message")

    nominated_node_name: str | None = Field(None, alias="nominatedNodeName")

    phase: str | None = Field(None, alias="phase")

    pod_ip: str | None = Field(None, alias="podIP")

    pod_i_ps: list[V1PodIP] | None = Field(None, alias="podIPs")

    qos_class: str | None = Field(None, alias="qosClass")

    reason: str | None = Field(None, alias="reason")

    resize: str | None = Field(None, alias="resize")

    resource_claim_statuses: list[V1PodResourceClaimStatus] | None = Field(
        None, alias="resourceClaimStatuses"
    )

    start_time: datetime | None = Field(None, alias="startTime")
