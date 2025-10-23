from pydantic import AliasChoices, BaseModel, Field
from .utils import _collection_if_none
from .utils import _default_if_none
from .utils import _exclude_if
from .v1_container_state import V1ContainerState
from .v1_container_user import V1ContainerUser
from .v1_resource_requirements import V1ResourceRequirements
from .v1_resource_status import V1ResourceStatus
from .v1_volume_mount_status import V1VolumeMountStatus
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1ContainerStatus",)


class V1ContainerStatus(BaseModel):
    allocated_resources: Annotated[
        dict[str, str], BeforeValidator(_collection_if_none("{}"))
    ] = Field(
        default={},
        serialization_alias="allocatedResources",
        validation_alias=AliasChoices("allocated_resources", "allocatedResources"),
        exclude_if=_exclude_if,
    )

    allocated_resources_status: Annotated[
        list[V1ResourceStatus], BeforeValidator(_collection_if_none("[]"))
    ] = Field(
        default=[],
        serialization_alias="allocatedResourcesStatus",
        validation_alias=AliasChoices(
            "allocated_resources_status", "allocatedResourcesStatus"
        ),
        exclude_if=_exclude_if,
    )

    container_id: str | None = Field(
        default=None,
        serialization_alias="containerID",
        validation_alias=AliasChoices("container_id", "containerID"),
        exclude_if=_exclude_if,
    )

    image: str | None = Field(default=None, exclude_if=_exclude_if)

    image_id: str | None = Field(
        default=None,
        serialization_alias="imageID",
        validation_alias=AliasChoices("image_id", "imageID"),
        exclude_if=_exclude_if,
    )

    last_state: Annotated[
        V1ContainerState, BeforeValidator(_default_if_none(V1ContainerState))
    ] = Field(
        default_factory=lambda: V1ContainerState(),
        serialization_alias="lastState",
        validation_alias=AliasChoices("last_state", "lastState"),
        exclude_if=_exclude_if,
    )

    name: str | None = Field(default=None, exclude_if=_exclude_if)

    ready: bool | None = Field(default=None, exclude_if=_exclude_if)

    resources: Annotated[
        V1ResourceRequirements,
        BeforeValidator(_default_if_none(V1ResourceRequirements)),
    ] = Field(default_factory=lambda: V1ResourceRequirements(), exclude_if=_exclude_if)

    restart_count: int | None = Field(
        default=None,
        serialization_alias="restartCount",
        validation_alias=AliasChoices("restart_count", "restartCount"),
        exclude_if=_exclude_if,
    )

    started: bool | None = Field(default=None, exclude_if=_exclude_if)

    state: Annotated[
        V1ContainerState, BeforeValidator(_default_if_none(V1ContainerState))
    ] = Field(default_factory=lambda: V1ContainerState(), exclude_if=_exclude_if)

    stop_signal: str | None = Field(
        default=None,
        serialization_alias="stopSignal",
        validation_alias=AliasChoices("stop_signal", "stopSignal"),
        exclude_if=_exclude_if,
    )

    user: Annotated[
        V1ContainerUser, BeforeValidator(_default_if_none(V1ContainerUser))
    ] = Field(default_factory=lambda: V1ContainerUser(), exclude_if=_exclude_if)

    volume_mounts: Annotated[
        list[V1VolumeMountStatus], BeforeValidator(_collection_if_none("[]"))
    ] = Field(
        default=[],
        serialization_alias="volumeMounts",
        validation_alias=AliasChoices("volume_mounts", "volumeMounts"),
        exclude_if=_exclude_if,
    )
