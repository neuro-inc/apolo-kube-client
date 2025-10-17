from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field
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

__all__ = ("V1Container",)


class V1Container(BaseModel):
    args: list[str] = Field(default=[])

    command: list[str] = Field(default=[])

    env: list[V1EnvVar] = Field(default=[])

    env_from: list[V1EnvFromSource] = Field(
        default=[],
        serialization_alias="envFrom",
        validation_alias=AliasChoices("env_from", "envFrom"),
    )

    image: str | None = Field(default=None)

    image_pull_policy: str | None = Field(
        default=None,
        serialization_alias="imagePullPolicy",
        validation_alias=AliasChoices("image_pull_policy", "imagePullPolicy"),
    )

    lifecycle: V1Lifecycle = Field(default_factory=lambda: V1Lifecycle())

    liveness_probe: V1Probe = Field(
        default_factory=lambda: V1Probe(),
        serialization_alias="livenessProbe",
        validation_alias=AliasChoices("liveness_probe", "livenessProbe"),
    )

    name: str | None = Field(default=None)

    ports: list[V1ContainerPort] = Field(default=[])

    readiness_probe: V1Probe = Field(
        default_factory=lambda: V1Probe(),
        serialization_alias="readinessProbe",
        validation_alias=AliasChoices("readiness_probe", "readinessProbe"),
    )

    resize_policy: list[V1ContainerResizePolicy] = Field(
        default=[],
        serialization_alias="resizePolicy",
        validation_alias=AliasChoices("resize_policy", "resizePolicy"),
    )

    resources: V1ResourceRequirements = Field(
        default_factory=lambda: V1ResourceRequirements()
    )

    restart_policy: str | None = Field(
        default=None,
        serialization_alias="restartPolicy",
        validation_alias=AliasChoices("restart_policy", "restartPolicy"),
    )

    restart_policy_rules: list[V1ContainerRestartRule] = Field(
        default=[],
        serialization_alias="restartPolicyRules",
        validation_alias=AliasChoices("restart_policy_rules", "restartPolicyRules"),
    )

    security_context: V1SecurityContext = Field(
        default_factory=lambda: V1SecurityContext(),
        serialization_alias="securityContext",
        validation_alias=AliasChoices("security_context", "securityContext"),
    )

    startup_probe: V1Probe = Field(
        default_factory=lambda: V1Probe(),
        serialization_alias="startupProbe",
        validation_alias=AliasChoices("startup_probe", "startupProbe"),
    )

    stdin: bool | None = Field(default=None)

    stdin_once: bool | None = Field(
        default=None,
        serialization_alias="stdinOnce",
        validation_alias=AliasChoices("stdin_once", "stdinOnce"),
    )

    termination_message_path: str | None = Field(
        default=None,
        serialization_alias="terminationMessagePath",
        validation_alias=AliasChoices(
            "termination_message_path", "terminationMessagePath"
        ),
    )

    termination_message_policy: str | None = Field(
        default=None,
        serialization_alias="terminationMessagePolicy",
        validation_alias=AliasChoices(
            "termination_message_policy", "terminationMessagePolicy"
        ),
    )

    tty: bool | None = Field(default=None)

    volume_devices: list[V1VolumeDevice] = Field(
        default=[],
        serialization_alias="volumeDevices",
        validation_alias=AliasChoices("volume_devices", "volumeDevices"),
    )

    volume_mounts: list[V1VolumeMount] = Field(
        default=[],
        serialization_alias="volumeMounts",
        validation_alias=AliasChoices("volume_mounts", "volumeMounts"),
    )

    working_dir: str | None = Field(
        default=None,
        serialization_alias="workingDir",
        validation_alias=AliasChoices("working_dir", "workingDir"),
    )
