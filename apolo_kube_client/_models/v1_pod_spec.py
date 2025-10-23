from pydantic import AliasChoices, BaseModel, Field
from .utils import _collection_if_none
from .utils import _default_if_none
from .utils import _exclude_if
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
        exclude_if=_exclude_if,
    )

    affinity: Annotated[V1Affinity, BeforeValidator(_default_if_none(V1Affinity))] = (
        Field(default_factory=lambda: V1Affinity(), exclude_if=_exclude_if)
    )

    automount_service_account_token: bool | None = Field(
        default=None,
        serialization_alias="automountServiceAccountToken",
        validation_alias=AliasChoices(
            "automount_service_account_token", "automountServiceAccountToken"
        ),
        exclude_if=_exclude_if,
    )

    containers: Annotated[
        list[V1Container], BeforeValidator(_collection_if_none("[]"))
    ] = Field(default=[], exclude_if=_exclude_if)

    dns_config: Annotated[
        V1PodDNSConfig, BeforeValidator(_default_if_none(V1PodDNSConfig))
    ] = Field(
        default_factory=lambda: V1PodDNSConfig(),
        serialization_alias="dnsConfig",
        validation_alias=AliasChoices("dns_config", "dnsConfig"),
        exclude_if=_exclude_if,
    )

    dns_policy: str | None = Field(
        default=None,
        serialization_alias="dnsPolicy",
        validation_alias=AliasChoices("dns_policy", "dnsPolicy"),
        exclude_if=_exclude_if,
    )

    enable_service_links: bool | None = Field(
        default=None,
        serialization_alias="enableServiceLinks",
        validation_alias=AliasChoices("enable_service_links", "enableServiceLinks"),
        exclude_if=_exclude_if,
    )

    ephemeral_containers: Annotated[
        list[V1EphemeralContainer], BeforeValidator(_collection_if_none("[]"))
    ] = Field(
        default=[],
        serialization_alias="ephemeralContainers",
        validation_alias=AliasChoices("ephemeral_containers", "ephemeralContainers"),
        exclude_if=_exclude_if,
    )

    host_aliases: Annotated[
        list[V1HostAlias], BeforeValidator(_collection_if_none("[]"))
    ] = Field(
        default=[],
        serialization_alias="hostAliases",
        validation_alias=AliasChoices("host_aliases", "hostAliases"),
        exclude_if=_exclude_if,
    )

    host_ipc: bool | None = Field(
        default=None,
        serialization_alias="hostIPC",
        validation_alias=AliasChoices("host_ipc", "hostIPC"),
        exclude_if=_exclude_if,
    )

    host_network: bool | None = Field(
        default=None,
        serialization_alias="hostNetwork",
        validation_alias=AliasChoices("host_network", "hostNetwork"),
        exclude_if=_exclude_if,
    )

    host_pid: bool | None = Field(
        default=None,
        serialization_alias="hostPID",
        validation_alias=AliasChoices("host_pid", "hostPID"),
        exclude_if=_exclude_if,
    )

    host_users: bool | None = Field(
        default=None,
        serialization_alias="hostUsers",
        validation_alias=AliasChoices("host_users", "hostUsers"),
        exclude_if=_exclude_if,
    )

    hostname: str | None = Field(default=None, exclude_if=_exclude_if)

    hostname_override: str | None = Field(
        default=None,
        serialization_alias="hostnameOverride",
        validation_alias=AliasChoices("hostname_override", "hostnameOverride"),
        exclude_if=_exclude_if,
    )

    image_pull_secrets: Annotated[
        list[V1LocalObjectReference], BeforeValidator(_collection_if_none("[]"))
    ] = Field(
        default=[],
        serialization_alias="imagePullSecrets",
        validation_alias=AliasChoices("image_pull_secrets", "imagePullSecrets"),
        exclude_if=_exclude_if,
    )

    init_containers: Annotated[
        list[V1Container], BeforeValidator(_collection_if_none("[]"))
    ] = Field(
        default=[],
        serialization_alias="initContainers",
        validation_alias=AliasChoices("init_containers", "initContainers"),
        exclude_if=_exclude_if,
    )

    node_name: str | None = Field(
        default=None,
        serialization_alias="nodeName",
        validation_alias=AliasChoices("node_name", "nodeName"),
        exclude_if=_exclude_if,
    )

    node_selector: Annotated[
        dict[str, str], BeforeValidator(_collection_if_none("{}"))
    ] = Field(
        default={},
        serialization_alias="nodeSelector",
        validation_alias=AliasChoices("node_selector", "nodeSelector"),
        exclude_if=_exclude_if,
    )

    os: Annotated[V1PodOS, BeforeValidator(_default_if_none(V1PodOS))] = Field(
        default_factory=lambda: V1PodOS(), exclude_if=_exclude_if
    )

    overhead: Annotated[dict[str, str], BeforeValidator(_collection_if_none("{}"))] = (
        Field(default={}, exclude_if=_exclude_if)
    )

    preemption_policy: str | None = Field(
        default=None,
        serialization_alias="preemptionPolicy",
        validation_alias=AliasChoices("preemption_policy", "preemptionPolicy"),
        exclude_if=_exclude_if,
    )

    priority: int | None = Field(default=None, exclude_if=_exclude_if)

    priority_class_name: str | None = Field(
        default=None,
        serialization_alias="priorityClassName",
        validation_alias=AliasChoices("priority_class_name", "priorityClassName"),
        exclude_if=_exclude_if,
    )

    readiness_gates: Annotated[
        list[V1PodReadinessGate], BeforeValidator(_collection_if_none("[]"))
    ] = Field(
        default=[],
        serialization_alias="readinessGates",
        validation_alias=AliasChoices("readiness_gates", "readinessGates"),
        exclude_if=_exclude_if,
    )

    resource_claims: Annotated[
        list[V1PodResourceClaim], BeforeValidator(_collection_if_none("[]"))
    ] = Field(
        default=[],
        serialization_alias="resourceClaims",
        validation_alias=AliasChoices("resource_claims", "resourceClaims"),
        exclude_if=_exclude_if,
    )

    resources: Annotated[
        V1ResourceRequirements,
        BeforeValidator(_default_if_none(V1ResourceRequirements)),
    ] = Field(default_factory=lambda: V1ResourceRequirements(), exclude_if=_exclude_if)

    restart_policy: str | None = Field(
        default=None,
        serialization_alias="restartPolicy",
        validation_alias=AliasChoices("restart_policy", "restartPolicy"),
        exclude_if=_exclude_if,
    )

    runtime_class_name: str | None = Field(
        default=None,
        serialization_alias="runtimeClassName",
        validation_alias=AliasChoices("runtime_class_name", "runtimeClassName"),
        exclude_if=_exclude_if,
    )

    scheduler_name: str | None = Field(
        default=None,
        serialization_alias="schedulerName",
        validation_alias=AliasChoices("scheduler_name", "schedulerName"),
        exclude_if=_exclude_if,
    )

    scheduling_gates: Annotated[
        list[V1PodSchedulingGate], BeforeValidator(_collection_if_none("[]"))
    ] = Field(
        default=[],
        serialization_alias="schedulingGates",
        validation_alias=AliasChoices("scheduling_gates", "schedulingGates"),
        exclude_if=_exclude_if,
    )

    security_context: Annotated[
        V1PodSecurityContext, BeforeValidator(_default_if_none(V1PodSecurityContext))
    ] = Field(
        default_factory=lambda: V1PodSecurityContext(),
        serialization_alias="securityContext",
        validation_alias=AliasChoices("security_context", "securityContext"),
        exclude_if=_exclude_if,
    )

    service_account: str | None = Field(
        default=None,
        serialization_alias="serviceAccount",
        validation_alias=AliasChoices("service_account", "serviceAccount"),
        exclude_if=_exclude_if,
    )

    service_account_name: str | None = Field(
        default=None,
        serialization_alias="serviceAccountName",
        validation_alias=AliasChoices("service_account_name", "serviceAccountName"),
        exclude_if=_exclude_if,
    )

    set_hostname_as_fqdn: bool | None = Field(
        default=None,
        serialization_alias="setHostnameAsFQDN",
        validation_alias=AliasChoices("set_hostname_as_fqdn", "setHostnameAsFQDN"),
        exclude_if=_exclude_if,
    )

    share_process_namespace: bool | None = Field(
        default=None,
        serialization_alias="shareProcessNamespace",
        validation_alias=AliasChoices(
            "share_process_namespace", "shareProcessNamespace"
        ),
        exclude_if=_exclude_if,
    )

    subdomain: str | None = Field(default=None, exclude_if=_exclude_if)

    termination_grace_period_seconds: int | None = Field(
        default=None,
        serialization_alias="terminationGracePeriodSeconds",
        validation_alias=AliasChoices(
            "termination_grace_period_seconds", "terminationGracePeriodSeconds"
        ),
        exclude_if=_exclude_if,
    )

    tolerations: Annotated[
        list[V1Toleration], BeforeValidator(_collection_if_none("[]"))
    ] = Field(default=[], exclude_if=_exclude_if)

    topology_spread_constraints: Annotated[
        list[V1TopologySpreadConstraint], BeforeValidator(_collection_if_none("[]"))
    ] = Field(
        default=[],
        serialization_alias="topologySpreadConstraints",
        validation_alias=AliasChoices(
            "topology_spread_constraints", "topologySpreadConstraints"
        ),
        exclude_if=_exclude_if,
    )

    volumes: Annotated[list[V1Volume], BeforeValidator(_collection_if_none("[]"))] = (
        Field(default=[], exclude_if=_exclude_if)
    )
