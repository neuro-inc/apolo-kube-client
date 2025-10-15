from pydantic import BaseModel, Field

from .v1_container_port import V1ContainerPort
from .v1_container_resize_policy import V1ContainerResizePolicy
from .v1_env_from_source import V1EnvFromSource
from .v1_env_var import V1EnvVar
from .v1_lifecycle import V1Lifecycle
from .v1_probe import V1Probe
from .v1_resource_requirements import V1ResourceRequirements
from .v1_security_context import V1SecurityContext
from .v1_volume_device import V1VolumeDevice
from .v1_volume_mount import V1VolumeMount


class V1EphemeralContainer(BaseModel):
    args: list[str] | None = Field(None, alias="args")

    command: list[str] | None = Field(None, alias="command")

    env: list[V1EnvVar] | None = Field(None, alias="env")

    env_from: list[V1EnvFromSource] | None = Field(None, alias="envFrom")

    image: str | None = Field(None, alias="image")

    image_pull_policy: str | None = Field(None, alias="imagePullPolicy")

    lifecycle: V1Lifecycle | None = Field(None, alias="lifecycle")

    liveness_probe: V1Probe | None = Field(None, alias="livenessProbe")

    name: str | None = Field(None, alias="name")

    ports: list[V1ContainerPort] | None = Field(None, alias="ports")

    readiness_probe: V1Probe | None = Field(None, alias="readinessProbe")

    resize_policy: list[V1ContainerResizePolicy] | None = Field(
        None, alias="resizePolicy"
    )

    resources: V1ResourceRequirements | None = Field(None, alias="resources")

    restart_policy: str | None = Field(None, alias="restartPolicy")

    security_context: V1SecurityContext | None = Field(None, alias="securityContext")

    startup_probe: V1Probe | None = Field(None, alias="startupProbe")

    stdin: bool | None = Field(None, alias="stdin")

    stdin_once: bool | None = Field(None, alias="stdinOnce")

    target_container_name: str | None = Field(None, alias="targetContainerName")

    termination_message_path: str | None = Field(None, alias="terminationMessagePath")

    termination_message_policy: str | None = Field(
        None, alias="terminationMessagePolicy"
    )

    tty: bool | None = Field(None, alias="tty")

    volume_devices: list[V1VolumeDevice] | None = Field(None, alias="volumeDevices")

    volume_mounts: list[V1VolumeMount] | None = Field(None, alias="volumeMounts")

    working_dir: str | None = Field(None, alias="workingDir")
