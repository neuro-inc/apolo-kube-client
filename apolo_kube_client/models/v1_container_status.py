from pydantic import BaseModel, Field

from .v1_container_state import V1ContainerState
from .v1_container_user import V1ContainerUser
from .v1_resource_requirements import V1ResourceRequirements
from .v1_resource_status import V1ResourceStatus
from .v1_volume_mount_status import V1VolumeMountStatus


class V1ContainerStatus(BaseModel):
    allocated_resources: dict(str, str) | None = Field(None, alias="allocatedResources")

    allocated_resources_status: list[V1ResourceStatus] | None = Field(
        None, alias="allocatedResourcesStatus"
    )

    container_id: str | None = Field(None, alias="containerID")

    image: str | None = Field(None, alias="image")

    image_id: str | None = Field(None, alias="imageID")

    last_state: V1ContainerState | None = Field(None, alias="lastState")

    name: str | None = Field(None, alias="name")

    ready: bool | None = Field(None, alias="ready")

    resources: V1ResourceRequirements | None = Field(None, alias="resources")

    restart_count: int | None = Field(None, alias="restartCount")

    started: bool | None = Field(None, alias="started")

    state: V1ContainerState | None = Field(None, alias="state")

    user: V1ContainerUser | None = Field(None, alias="user")

    volume_mounts: list[V1VolumeMountStatus] | None = Field(None, alias="volumeMounts")
