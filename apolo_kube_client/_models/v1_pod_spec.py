from pydantic import AliasChoices, BaseModel, Field
from .base import _default_if_none
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
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1PodSpec",)


class V1PodSpec(BaseModel):
    active_deadline_seconds: int | None = Field(
        default=None,
        serialization_alias="activeDeadlineSeconds",
        validation_alias=AliasChoices(
            "active_deadline_seconds", "activeDeadlineSeconds"
        ),
    )

    affinity: Annotated[V1Affinity, BeforeValidator(_default_if_none(V1Affinity))] = (
        Field(default_factory=lambda: V1Affinity())
    )

    automount_service_account_token: bool | None = Field(
        default=None,
        serialization_alias="automountServiceAccountToken",
        validation_alias=AliasChoices(
            "automount_service_account_token", "automountServiceAccountToken"
        ),
    )

    containers: list[V1Container] = []

    dns_config: Annotated[
        V1PodDNSConfig, BeforeValidator(_default_if_none(V1PodDNSConfig))
    ] = Field(
        default_factory=lambda: V1PodDNSConfig(),
        serialization_alias="dnsConfig",
        validation_alias=AliasChoices("dns_config", "dnsConfig"),
    )

    dns_policy: str | None = Field(
        default=None,
        serialization_alias="dnsPolicy",
        validation_alias=AliasChoices("dns_policy", "dnsPolicy"),
    )

    enable_service_links: bool | None = Field(
        default=None,
        serialization_alias="enableServiceLinks",
        validation_alias=AliasChoices("enable_service_links", "enableServiceLinks"),
    )

    ephemeral_containers: list[V1EphemeralContainer] = Field(
        default=[],
        serialization_alias="ephemeralContainers",
        validation_alias=AliasChoices("ephemeral_containers", "ephemeralContainers"),
    )

    host_aliases: list[V1HostAlias] = Field(
        default=[],
        serialization_alias="hostAliases",
        validation_alias=AliasChoices("host_aliases", "hostAliases"),
    )

    host_ipc: bool | None = Field(
        default=None,
        serialization_alias="hostIPC",
        validation_alias=AliasChoices("host_ipc", "hostIPC"),
    )

    host_network: bool | None = Field(
        default=None,
        serialization_alias="hostNetwork",
        validation_alias=AliasChoices("host_network", "hostNetwork"),
    )

    host_pid: bool | None = Field(
        default=None,
        serialization_alias="hostPID",
        validation_alias=AliasChoices("host_pid", "hostPID"),
    )

    host_users: bool | None = Field(
        default=None,
        serialization_alias="hostUsers",
        validation_alias=AliasChoices("host_users", "hostUsers"),
    )

    hostname: str | None = None

    hostname_override: str | None = Field(
        default=None,
        serialization_alias="hostnameOverride",
        validation_alias=AliasChoices("hostname_override", "hostnameOverride"),
    )

    image_pull_secrets: list[V1LocalObjectReference] = Field(
        default=[],
        serialization_alias="imagePullSecrets",
        validation_alias=AliasChoices("image_pull_secrets", "imagePullSecrets"),
    )

    init_containers: list[V1Container] = Field(
        default=[],
        serialization_alias="initContainers",
        validation_alias=AliasChoices("init_containers", "initContainers"),
    )

    node_name: str | None = Field(
        default=None,
        serialization_alias="nodeName",
        validation_alias=AliasChoices("node_name", "nodeName"),
    )

    node_selector: dict[str, str] = Field(
        default={},
        serialization_alias="nodeSelector",
        validation_alias=AliasChoices("node_selector", "nodeSelector"),
    )

    os: Annotated[V1PodOS, BeforeValidator(_default_if_none(V1PodOS))] = Field(
        default_factory=lambda: V1PodOS()
    )

    overhead: dict[str, str] = {}

    preemption_policy: str | None = Field(
        default=None,
        serialization_alias="preemptionPolicy",
        validation_alias=AliasChoices("preemption_policy", "preemptionPolicy"),
    )

    priority: int | None = None

    priority_class_name: str | None = Field(
        default=None,
        serialization_alias="priorityClassName",
        validation_alias=AliasChoices("priority_class_name", "priorityClassName"),
    )

    readiness_gates: list[V1PodReadinessGate] = Field(
        default=[],
        serialization_alias="readinessGates",
        validation_alias=AliasChoices("readiness_gates", "readinessGates"),
    )

    resource_claims: list[V1PodResourceClaim] = Field(
        default=[],
        serialization_alias="resourceClaims",
        validation_alias=AliasChoices("resource_claims", "resourceClaims"),
    )

    resources: Annotated[
        V1ResourceRequirements,
        BeforeValidator(_default_if_none(V1ResourceRequirements)),
    ] = Field(default_factory=lambda: V1ResourceRequirements())

    restart_policy: str | None = Field(
        default=None,
        serialization_alias="restartPolicy",
        validation_alias=AliasChoices("restart_policy", "restartPolicy"),
    )

    runtime_class_name: str | None = Field(
        default=None,
        serialization_alias="runtimeClassName",
        validation_alias=AliasChoices("runtime_class_name", "runtimeClassName"),
    )

    scheduler_name: str | None = Field(
        default=None,
        serialization_alias="schedulerName",
        validation_alias=AliasChoices("scheduler_name", "schedulerName"),
    )

    scheduling_gates: list[V1PodSchedulingGate] = Field(
        default=[],
        serialization_alias="schedulingGates",
        validation_alias=AliasChoices("scheduling_gates", "schedulingGates"),
    )

    security_context: Annotated[
        V1PodSecurityContext, BeforeValidator(_default_if_none(V1PodSecurityContext))
    ] = Field(
        default_factory=lambda: V1PodSecurityContext(),
        serialization_alias="securityContext",
        validation_alias=AliasChoices("security_context", "securityContext"),
    )

    service_account: str | None = Field(
        default=None,
        serialization_alias="serviceAccount",
        validation_alias=AliasChoices("service_account", "serviceAccount"),
    )

    service_account_name: str | None = Field(
        default=None,
        serialization_alias="serviceAccountName",
        validation_alias=AliasChoices("service_account_name", "serviceAccountName"),
    )

    set_hostname_as_fqdn: bool | None = Field(
        default=None,
        serialization_alias="setHostnameAsFQDN",
        validation_alias=AliasChoices("set_hostname_as_fqdn", "setHostnameAsFQDN"),
    )

    share_process_namespace: bool | None = Field(
        default=None,
        serialization_alias="shareProcessNamespace",
        validation_alias=AliasChoices(
            "share_process_namespace", "shareProcessNamespace"
        ),
    )

    subdomain: str | None = None

    termination_grace_period_seconds: int | None = Field(
        default=None,
        serialization_alias="terminationGracePeriodSeconds",
        validation_alias=AliasChoices(
            "termination_grace_period_seconds", "terminationGracePeriodSeconds"
        ),
    )

    tolerations: list[V1Toleration] = []

    topology_spread_constraints: list[V1TopologySpreadConstraint] = Field(
        default=[],
        serialization_alias="topologySpreadConstraints",
        validation_alias=AliasChoices(
            "topology_spread_constraints", "topologySpreadConstraints"
        ),
    )

    volumes: list[V1Volume] = []
