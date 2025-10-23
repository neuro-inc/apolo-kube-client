from pydantic import AliasChoices, BaseModel, Field
from .utils import _collection_if_none
from .utils import _default_if_none
from .utils import _exclude_if
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
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1EphemeralContainer",)


class V1EphemeralContainer(BaseModel):
    args: Annotated[list[str], BeforeValidator(_collection_if_none("[]"))] = Field(
        default=[], exclude_if=_exclude_if
    )

    command: Annotated[list[str], BeforeValidator(_collection_if_none("[]"))] = Field(
        default=[], exclude_if=_exclude_if
    )

    env: Annotated[list[V1EnvVar], BeforeValidator(_collection_if_none("[]"))] = Field(
        default=[], exclude_if=_exclude_if
    )

    env_from: Annotated[
        list[V1EnvFromSource], BeforeValidator(_collection_if_none("[]"))
    ] = Field(
        default=[],
        serialization_alias="envFrom",
        validation_alias=AliasChoices("env_from", "envFrom"),
        exclude_if=_exclude_if,
    )

    image: str | None = Field(default=None, exclude_if=_exclude_if)

    image_pull_policy: str | None = Field(
        default=None,
        serialization_alias="imagePullPolicy",
        validation_alias=AliasChoices("image_pull_policy", "imagePullPolicy"),
        exclude_if=_exclude_if,
    )

    lifecycle: Annotated[
        V1Lifecycle, BeforeValidator(_default_if_none(V1Lifecycle))
    ] = Field(default_factory=lambda: V1Lifecycle(), exclude_if=_exclude_if)

    liveness_probe: Annotated[V1Probe, BeforeValidator(_default_if_none(V1Probe))] = (
        Field(
            default_factory=lambda: V1Probe(),
            serialization_alias="livenessProbe",
            validation_alias=AliasChoices("liveness_probe", "livenessProbe"),
            exclude_if=_exclude_if,
        )
    )

    name: str | None = Field(default=None, exclude_if=_exclude_if)

    ports: Annotated[
        list[V1ContainerPort], BeforeValidator(_collection_if_none("[]"))
    ] = Field(default=[], exclude_if=_exclude_if)

    readiness_probe: Annotated[V1Probe, BeforeValidator(_default_if_none(V1Probe))] = (
        Field(
            default_factory=lambda: V1Probe(),
            serialization_alias="readinessProbe",
            validation_alias=AliasChoices("readiness_probe", "readinessProbe"),
            exclude_if=_exclude_if,
        )
    )

    resize_policy: Annotated[
        list[V1ContainerResizePolicy], BeforeValidator(_collection_if_none("[]"))
    ] = Field(
        default=[],
        serialization_alias="resizePolicy",
        validation_alias=AliasChoices("resize_policy", "resizePolicy"),
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

    restart_policy_rules: Annotated[
        list[V1ContainerRestartRule], BeforeValidator(_collection_if_none("[]"))
    ] = Field(
        default=[],
        serialization_alias="restartPolicyRules",
        validation_alias=AliasChoices("restart_policy_rules", "restartPolicyRules"),
        exclude_if=_exclude_if,
    )

    security_context: Annotated[
        V1SecurityContext, BeforeValidator(_default_if_none(V1SecurityContext))
    ] = Field(
        default_factory=lambda: V1SecurityContext(),
        serialization_alias="securityContext",
        validation_alias=AliasChoices("security_context", "securityContext"),
        exclude_if=_exclude_if,
    )

    startup_probe: Annotated[V1Probe, BeforeValidator(_default_if_none(V1Probe))] = (
        Field(
            default_factory=lambda: V1Probe(),
            serialization_alias="startupProbe",
            validation_alias=AliasChoices("startup_probe", "startupProbe"),
            exclude_if=_exclude_if,
        )
    )

    stdin: bool | None = Field(default=None, exclude_if=_exclude_if)

    stdin_once: bool | None = Field(
        default=None,
        serialization_alias="stdinOnce",
        validation_alias=AliasChoices("stdin_once", "stdinOnce"),
        exclude_if=_exclude_if,
    )

    target_container_name: str | None = Field(
        default=None,
        serialization_alias="targetContainerName",
        validation_alias=AliasChoices("target_container_name", "targetContainerName"),
        exclude_if=_exclude_if,
    )

    termination_message_path: str | None = Field(
        default=None,
        serialization_alias="terminationMessagePath",
        validation_alias=AliasChoices(
            "termination_message_path", "terminationMessagePath"
        ),
        exclude_if=_exclude_if,
    )

    termination_message_policy: str | None = Field(
        default=None,
        serialization_alias="terminationMessagePolicy",
        validation_alias=AliasChoices(
            "termination_message_policy", "terminationMessagePolicy"
        ),
        exclude_if=_exclude_if,
    )

    tty: bool | None = Field(default=None, exclude_if=_exclude_if)

    volume_devices: Annotated[
        list[V1VolumeDevice], BeforeValidator(_collection_if_none("[]"))
    ] = Field(
        default=[],
        serialization_alias="volumeDevices",
        validation_alias=AliasChoices("volume_devices", "volumeDevices"),
        exclude_if=_exclude_if,
    )

    volume_mounts: Annotated[
        list[V1VolumeMount], BeforeValidator(_collection_if_none("[]"))
    ] = Field(
        default=[],
        serialization_alias="volumeMounts",
        validation_alias=AliasChoices("volume_mounts", "volumeMounts"),
        exclude_if=_exclude_if,
    )

    working_dir: str | None = Field(
        default=None,
        serialization_alias="workingDir",
        validation_alias=AliasChoices("working_dir", "workingDir"),
        exclude_if=_exclude_if,
    )
