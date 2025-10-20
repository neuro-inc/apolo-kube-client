from pydantic import AliasChoices, BaseModel, Field
from .v1_container_state import V1ContainerState
from .v1_container_user import V1ContainerUser
from .v1_resource_requirements import V1ResourceRequirements
from .v1_resource_status import V1ResourceStatus
from .v1_volume_mount_status import V1VolumeMountStatus

__all__ = ("V1ContainerStatus",)


class V1ContainerStatus(BaseModel):
    allocated_resources: dict[str, str] = Field(
        default={},
        serialization_alias="allocatedResources",
        validation_alias=AliasChoices("allocated_resources", "allocatedResources"),
    )

    allocated_resources_status: list[V1ResourceStatus] = Field(
        default=[],
        serialization_alias="allocatedResourcesStatus",
        validation_alias=AliasChoices(
            "allocated_resources_status", "allocatedResourcesStatus"
        ),
    )

    container_id: str | None = Field(
        default=None,
        serialization_alias="containerID",
        validation_alias=AliasChoices("container_id", "containerID"),
    )

    image: str | None = None

    image_id: str | None = Field(
        default=None,
        serialization_alias="imageID",
        validation_alias=AliasChoices("image_id", "imageID"),
    )

    last_state: V1ContainerState = Field(
        default_factory=lambda: V1ContainerState(),
        serialization_alias="lastState",
        validation_alias=AliasChoices("last_state", "lastState"),
    )

    name: str | None = None

    ready: bool | None = None

    resources: V1ResourceRequirements = Field(
        default_factory=lambda: V1ResourceRequirements()
    )

    restart_count: int | None = Field(
        default=None,
        serialization_alias="restartCount",
        validation_alias=AliasChoices("restart_count", "restartCount"),
    )

    started: bool | None = None

    state: V1ContainerState = Field(default_factory=lambda: V1ContainerState())

    stop_signal: str | None = Field(
        default=None,
        serialization_alias="stopSignal",
        validation_alias=AliasChoices("stop_signal", "stopSignal"),
    )

    user: V1ContainerUser = Field(default_factory=lambda: V1ContainerUser())

    volume_mounts: list[V1VolumeMountStatus] = Field(
        default=[],
        serialization_alias="volumeMounts",
        validation_alias=AliasChoices("volume_mounts", "volumeMounts"),
    )
