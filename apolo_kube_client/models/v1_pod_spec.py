from __future__ import annotations

from pydantic import BaseModel, Field

from .v1_affinity import V1Affinity
from .v1_container import V1Container
from .v1_ephemeral_container import V1EphemeralContainer
from .v1_host_alias import V1HostAlias
from .v1_local_object_reference import V1LocalObjectReference
from .v1_pod_dns_config import V1PodDNSConfig
from .v1_pod_os import V1PodOS
from .v1_pod_readiness_gate import V1PodReadinessGate
from .v1_pod_resource_claim import V1PodResourceClaim
from .v1_pod_scheduling_gate import V1PodSchedulingGate
from .v1_pod_security_context import V1PodSecurityContext
from .v1_resource_requirements import V1ResourceRequirements
from .v1_toleration import V1Toleration
from .v1_topology_spread_constraint import V1TopologySpreadConstraint
from .v1_volume import V1Volume

__all__ = ("V1PodSpec",)


class V1PodSpec(BaseModel):
    active_deadline_seconds: int | None = Field(None, alias="activeDeadlineSeconds")

    affinity: V1Affinity | None = Field(None, alias="affinity")

    automount_service_account_token: bool | None = Field(
        None, alias="automountServiceAccountToken"
    )

    containers: list[V1Container] | None = Field(None, alias="containers")

    dns_config: V1PodDNSConfig | None = Field(None, alias="dnsConfig")

    dns_policy: str | None = Field(None, alias="dnsPolicy")

    enable_service_links: bool | None = Field(None, alias="enableServiceLinks")

    ephemeral_containers: list[V1EphemeralContainer] | None = Field(
        None, alias="ephemeralContainers"
    )

    host_aliases: list[V1HostAlias] | None = Field(None, alias="hostAliases")

    host_ipc: bool | None = Field(None, alias="hostIPC")

    host_network: bool | None = Field(None, alias="hostNetwork")

    host_pid: bool | None = Field(None, alias="hostPID")

    host_users: bool | None = Field(None, alias="hostUsers")

    hostname: str | None = Field(None, alias="hostname")

    image_pull_secrets: list[V1LocalObjectReference] | None = Field(
        None, alias="imagePullSecrets"
    )

    init_containers: list[V1Container] | None = Field(None, alias="initContainers")

    node_name: str | None = Field(None, alias="nodeName")

    node_selector: dict[str, str] | None = Field(None, alias="nodeSelector")

    os: V1PodOS | None = Field(None, alias="os")

    overhead: dict[str, str] | None = Field(None, alias="overhead")

    preemption_policy: str | None = Field(None, alias="preemptionPolicy")

    priority: int | None = Field(None, alias="priority")

    priority_class_name: str | None = Field(None, alias="priorityClassName")

    readiness_gates: list[V1PodReadinessGate] | None = Field(
        None, alias="readinessGates"
    )

    resource_claims: list[V1PodResourceClaim] | None = Field(
        None, alias="resourceClaims"
    )

    resources: V1ResourceRequirements | None = Field(None, alias="resources")

    restart_policy: str | None = Field(None, alias="restartPolicy")

    runtime_class_name: str | None = Field(None, alias="runtimeClassName")

    scheduler_name: str | None = Field(None, alias="schedulerName")

    scheduling_gates: list[V1PodSchedulingGate] | None = Field(
        None, alias="schedulingGates"
    )

    security_context: V1PodSecurityContext | None = Field(None, alias="securityContext")

    service_account: str | None = Field(None, alias="serviceAccount")

    service_account_name: str | None = Field(None, alias="serviceAccountName")

    set_hostname_as_fqdn: bool | None = Field(None, alias="setHostnameAsFQDN")

    share_process_namespace: bool | None = Field(None, alias="shareProcessNamespace")

    subdomain: str | None = Field(None, alias="subdomain")

    termination_grace_period_seconds: int | None = Field(
        None, alias="terminationGracePeriodSeconds"
    )

    tolerations: list[V1Toleration] | None = Field(None, alias="tolerations")

    topology_spread_constraints: list[V1TopologySpreadConstraint] | None = Field(
        None, alias="topologySpreadConstraints"
    )

    volumes: list[V1Volume] | None = Field(None, alias="volumes")
