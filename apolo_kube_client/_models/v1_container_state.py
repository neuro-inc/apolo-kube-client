from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from .utils import _default_if_none
from .v1_container_state_running import V1ContainerStateRunning
from .v1_container_state_terminated import V1ContainerStateTerminated
from .v1_container_state_waiting import V1ContainerStateWaiting
from pydantic import BeforeValidator

__all__ = ("V1ContainerState",)


class V1ContainerState(BaseModel):
    """ContainerState holds a possible state of container. Only one of its members may be specified. If none of them is specified, the default one is ContainerStateWaiting."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.core.v1.ContainerState"

    running: Annotated[
        V1ContainerStateRunning,
        Field(
            description="""Details about a running container""",
            exclude_if=lambda v: not v.__pydantic_fields_set__,
        ),
        BeforeValidator(_default_if_none(V1ContainerStateRunning)),
    ] = V1ContainerStateRunning()

    terminated: Annotated[
        V1ContainerStateTerminated | None,
        Field(
            description="""Details about a terminated container""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    waiting: Annotated[
        V1ContainerStateWaiting,
        Field(
            description="""Details about a waiting container""",
            exclude_if=lambda v: not v.__pydantic_fields_set__,
        ),
        BeforeValidator(_default_if_none(V1ContainerStateWaiting)),
    ] = V1ContainerStateWaiting()
