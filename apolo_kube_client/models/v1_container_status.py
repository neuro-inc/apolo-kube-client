from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_container_state import V1ContainerState
from .v1_container_user import V1ContainerUser
from .v1_resource_requirements import V1ResourceRequirements
from .v1_resource_status import V1ResourceStatus
from .v1_volume_mount_status import V1VolumeMountStatus

__all__ = ("V1ContainerStatus",)


class V1ContainerStatus(BaseModel):
    allocated_resources: dict[str, str] = Field(
        default_factory=lambda: {}, alias="allocatedResources"
    )

    allocated_resources_status: list[V1ResourceStatus] = Field(
        default_factory=lambda: [], alias="allocatedResourcesStatus"
    )

    container_id: str | None = Field(default_factory=lambda: None, alias="containerID")

    image: str | None = Field(default_factory=lambda: None)

    image_id: str | None = Field(default_factory=lambda: None, alias="imageID")

    last_state: V1ContainerState = Field(
        default_factory=lambda: V1ContainerState(), alias="lastState"
    )

    name: str | None = Field(default_factory=lambda: None)

    ready: bool | None = Field(default_factory=lambda: None)

    resources: V1ResourceRequirements = Field(
        default_factory=lambda: V1ResourceRequirements()
    )

    restart_count: int | None = Field(
        default_factory=lambda: None, alias="restartCount"
    )

    started: bool | None = Field(default_factory=lambda: None)

    state: V1ContainerState = Field(default_factory=lambda: V1ContainerState())

    stop_signal: str | None = Field(default_factory=lambda: None, alias="stopSignal")

    user: V1ContainerUser = Field(default_factory=lambda: V1ContainerUser())

    volume_mounts: list[V1VolumeMountStatus] = Field(
        default_factory=lambda: [], alias="volumeMounts"
    )
