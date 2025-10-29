from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from .utils import _collection_if_none
from .utils import _default_if_none
from .v1_container_state import V1ContainerState
from .v1_container_user import V1ContainerUser
from .v1_resource_requirements import V1ResourceRequirements
from .v1_resource_status import V1ResourceStatus
from .v1_volume_mount_status import V1VolumeMountStatus
from pydantic import BeforeValidator

__all__ = ("V1ContainerStatus",)


class V1ContainerStatus(BaseModel):
    """ContainerStatus contains details for the current status of this container."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.core.v1.ContainerStatus"

    allocated_resources: Annotated[
        dict[str, str],
        Field(
            alias="allocatedResources",
            description="""AllocatedResources represents the compute resources allocated for this container by the node. Kubelet sets this value to Container.Resources.Requests upon successful pod admission and after successfully admitting desired pod resize.""",
            exclude_if=lambda v: v == {},
        ),
        BeforeValidator(_collection_if_none("{}")),
    ] = {}

    allocated_resources_status: Annotated[
        list[V1ResourceStatus],
        Field(
            alias="allocatedResourcesStatus",
            description="""AllocatedResourcesStatus represents the status of various resources allocated for this Pod.""",
            exclude_if=lambda v: v == [],
        ),
        BeforeValidator(_collection_if_none("[]")),
    ] = []

    container_id: Annotated[
        str | None,
        Field(
            alias="containerID",
            description="""ContainerID is the ID of the container in the format '<type>://<container_id>'. Where type is a container runtime identifier, returned from Version call of CRI API (for example "containerd").""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    image: Annotated[
        str,
        Field(
            description="""Image is the name of container image that the container is running. The container image may not match the image used in the PodSpec, as it may have been resolved by the runtime. More info: https://kubernetes.io/docs/concepts/containers/images."""
        ),
    ]

    image_id: Annotated[
        str,
        Field(
            alias="imageID",
            description="""ImageID is the image ID of the container's image. The image ID may not match the image ID of the image used in the PodSpec, as it may have been resolved by the runtime.""",
        ),
    ]

    last_state: Annotated[
        V1ContainerState,
        Field(
            alias="lastState",
            description="""LastTerminationState holds the last termination state of the container to help debug container crashes and restarts. This field is not populated if the container is still running and RestartCount is 0.""",
            exclude_if=lambda v: not v.__pydantic_fields_set__,
        ),
        BeforeValidator(_default_if_none(V1ContainerState)),
    ] = V1ContainerState()

    name: Annotated[
        str,
        Field(
            description="""Name is a DNS_LABEL representing the unique name of the container. Each container in a pod must have a unique name across all container types. Cannot be updated."""
        ),
    ]

    ready: Annotated[
        bool,
        Field(
            description="""Ready specifies whether the container is currently passing its readiness check. The value will change as readiness probes keep executing. If no readiness probes are specified, this field defaults to true once the container is fully started (see Started field).

The value is typically used to determine whether a container is ready to accept traffic."""
        ),
    ]

    resources: Annotated[
        V1ResourceRequirements,
        Field(
            description="""Resources represents the compute resource requests and limits that have been successfully enacted on the running container after it has been started or has been successfully resized.""",
            exclude_if=lambda v: not v.__pydantic_fields_set__,
        ),
        BeforeValidator(_default_if_none(V1ResourceRequirements)),
    ] = V1ResourceRequirements()

    restart_count: Annotated[
        int,
        Field(
            alias="restartCount",
            description="""RestartCount holds the number of times the container has been restarted. Kubelet makes an effort to always increment the value, but there are cases when the state may be lost due to node restarts and then the value may be reset to 0. The value is never negative.""",
        ),
    ]

    started: Annotated[
        bool | None,
        Field(
            description="""Started indicates whether the container has finished its postStart lifecycle hook and passed its startup probe. Initialized as false, becomes true after startupProbe is considered successful. Resets to false when the container is restarted, or if kubelet loses state temporarily. In both cases, startup probes will run again. Is always true when no startupProbe is defined and container is running and has passed the postStart lifecycle hook. The null value must be treated the same as false.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    state: Annotated[
        V1ContainerState,
        Field(
            description="""State holds details about the container's current condition.""",
            exclude_if=lambda v: not v.__pydantic_fields_set__,
        ),
        BeforeValidator(_default_if_none(V1ContainerState)),
    ] = V1ContainerState()

    stop_signal: Annotated[
        str | None,
        Field(
            alias="stopSignal",
            description="""StopSignal reports the effective stop signal for this container""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    user: Annotated[
        V1ContainerUser,
        Field(
            description="""User represents user identity information initially attached to the first process of the container""",
            exclude_if=lambda v: not v.__pydantic_fields_set__,
        ),
        BeforeValidator(_default_if_none(V1ContainerUser)),
    ] = V1ContainerUser()

    volume_mounts: Annotated[
        list[V1VolumeMountStatus],
        Field(
            alias="volumeMounts",
            description="""Status of volume mounts.""",
            exclude_if=lambda v: v == [],
        ),
        BeforeValidator(_collection_if_none("[]")),
    ] = []
