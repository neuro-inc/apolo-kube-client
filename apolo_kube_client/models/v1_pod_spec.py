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
    active_deadline_seconds: int | None = Field(
        default_factory=lambda: None, alias="activeDeadlineSeconds"
    )

    affinity: V1Affinity = Field(default_factory=lambda: V1Affinity())

    automount_service_account_token: bool | None = Field(
        default_factory=lambda: None, alias="automountServiceAccountToken"
    )

    containers: list[V1Container] = Field(default_factory=lambda: [])

    dns_config: V1PodDNSConfig = Field(
        default_factory=lambda: V1PodDNSConfig(), alias="dnsConfig"
    )

    dns_policy: str | None = Field(default_factory=lambda: None, alias="dnsPolicy")

    enable_service_links: bool | None = Field(
        default_factory=lambda: None, alias="enableServiceLinks"
    )

    ephemeral_containers: list[V1EphemeralContainer] = Field(
        default_factory=lambda: [], alias="ephemeralContainers"
    )

    host_aliases: list[V1HostAlias] = Field(
        default_factory=lambda: [], alias="hostAliases"
    )

    host_ipc: bool | None = Field(default_factory=lambda: None, alias="hostIPC")

    host_network: bool | None = Field(default_factory=lambda: None, alias="hostNetwork")

    host_pid: bool | None = Field(default_factory=lambda: None, alias="hostPID")

    host_users: bool | None = Field(default_factory=lambda: None, alias="hostUsers")

    hostname: str | None = Field(default_factory=lambda: None)

    hostname_override: str | None = Field(
        default_factory=lambda: None, alias="hostnameOverride"
    )

    image_pull_secrets: list[V1LocalObjectReference] = Field(
        default_factory=lambda: [], alias="imagePullSecrets"
    )

    init_containers: list[V1Container] = Field(
        default_factory=lambda: [], alias="initContainers"
    )

    node_name: str | None = Field(default_factory=lambda: None, alias="nodeName")

    node_selector: dict[str, str] = Field(
        default_factory=lambda: {}, alias="nodeSelector"
    )

    os: V1PodOS = Field(default_factory=lambda: V1PodOS())

    overhead: dict[str, str] = Field(default_factory=lambda: {})

    preemption_policy: str | None = Field(
        default_factory=lambda: None, alias="preemptionPolicy"
    )

    priority: int | None = Field(default_factory=lambda: None)

    priority_class_name: str | None = Field(
        default_factory=lambda: None, alias="priorityClassName"
    )

    readiness_gates: list[V1PodReadinessGate] = Field(
        default_factory=lambda: [], alias="readinessGates"
    )

    resource_claims: list[V1PodResourceClaim] = Field(
        default_factory=lambda: [], alias="resourceClaims"
    )

    resources: V1ResourceRequirements = Field(
        default_factory=lambda: V1ResourceRequirements()
    )

    restart_policy: str | None = Field(
        default_factory=lambda: None, alias="restartPolicy"
    )

    runtime_class_name: str | None = Field(
        default_factory=lambda: None, alias="runtimeClassName"
    )

    scheduler_name: str | None = Field(
        default_factory=lambda: None, alias="schedulerName"
    )

    scheduling_gates: list[V1PodSchedulingGate] = Field(
        default_factory=lambda: [], alias="schedulingGates"
    )

    security_context: V1PodSecurityContext = Field(
        default_factory=lambda: V1PodSecurityContext(), alias="securityContext"
    )

    service_account: str | None = Field(
        default_factory=lambda: None, alias="serviceAccount"
    )

    service_account_name: str | None = Field(
        default_factory=lambda: None, alias="serviceAccountName"
    )

    set_hostname_as_fqdn: bool | None = Field(
        default_factory=lambda: None, alias="setHostnameAsFQDN"
    )

    share_process_namespace: bool | None = Field(
        default_factory=lambda: None, alias="shareProcessNamespace"
    )

    subdomain: str | None = Field(default_factory=lambda: None)

    termination_grace_period_seconds: int | None = Field(
        default_factory=lambda: None, alias="terminationGracePeriodSeconds"
    )

    tolerations: list[V1Toleration] = Field(default_factory=lambda: [])

    topology_spread_constraints: list[V1TopologySpreadConstraint] = Field(
        default_factory=lambda: [], alias="topologySpreadConstraints"
    )

    volumes: list[V1Volume] = Field(default_factory=lambda: [])
