from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_container_port import V1ContainerPort
from .v1_container_resize_policy import V1ContainerResizePolicy
from .v1_container_restart_rule import V1ContainerRestartRule
from .v1_env_from_source import V1EnvFromSource
from .v1_env_var import V1EnvVar
from .v1_lifecycle import V1Lifecycle
from .v1_probe import V1Probe
from .v1_resource_requirements import V1ResourceRequirements
from .v1_security_context import V1SecurityContext
from .v1_volume_device import V1VolumeDevice
from .v1_volume_mount import V1VolumeMount

__all__ = ("V1EphemeralContainer",)


class V1EphemeralContainer(BaseModel):
    args: list[str] = Field(default_factory=lambda: [], alias="args")

    command: list[str] = Field(default_factory=lambda: [], alias="command")

    env: list[V1EnvVar] = Field(default_factory=lambda: [], alias="env")

    env_from: list[V1EnvFromSource] = Field(default_factory=lambda: [], alias="envFrom")

    image: str | None = Field(default_factory=lambda: None, alias="image")

    image_pull_policy: str | None = Field(
        default_factory=lambda: None, alias="imagePullPolicy"
    )

    lifecycle: V1Lifecycle = Field(
        default_factory=lambda: V1Lifecycle(), alias="lifecycle"
    )

    liveness_probe: V1Probe = Field(
        default_factory=lambda: V1Probe(), alias="livenessProbe"
    )

    name: str | None = Field(default_factory=lambda: None, alias="name")

    ports: list[V1ContainerPort] = Field(default_factory=lambda: [], alias="ports")

    readiness_probe: V1Probe = Field(
        default_factory=lambda: V1Probe(), alias="readinessProbe"
    )

    resize_policy: list[V1ContainerResizePolicy] = Field(
        default_factory=lambda: [], alias="resizePolicy"
    )

    resources: V1ResourceRequirements = Field(
        default_factory=lambda: V1ResourceRequirements(), alias="resources"
    )

    restart_policy: str | None = Field(
        default_factory=lambda: None, alias="restartPolicy"
    )

    restart_policy_rules: list[V1ContainerRestartRule] = Field(
        default_factory=lambda: [], alias="restartPolicyRules"
    )

    security_context: V1SecurityContext = Field(
        default_factory=lambda: V1SecurityContext(), alias="securityContext"
    )

    startup_probe: V1Probe = Field(
        default_factory=lambda: V1Probe(), alias="startupProbe"
    )

    stdin: bool | None = Field(default_factory=lambda: None, alias="stdin")

    stdin_once: bool | None = Field(default_factory=lambda: None, alias="stdinOnce")

    target_container_name: str | None = Field(
        default_factory=lambda: None, alias="targetContainerName"
    )

    termination_message_path: str | None = Field(
        default_factory=lambda: None, alias="terminationMessagePath"
    )

    termination_message_policy: str | None = Field(
        default_factory=lambda: None, alias="terminationMessagePolicy"
    )

    tty: bool | None = Field(default_factory=lambda: None, alias="tty")

    volume_devices: list[V1VolumeDevice] = Field(
        default_factory=lambda: [], alias="volumeDevices"
    )

    volume_mounts: list[V1VolumeMount] = Field(
        default_factory=lambda: [], alias="volumeMounts"
    )

    working_dir: str | None = Field(default_factory=lambda: None, alias="workingDir")
