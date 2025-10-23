from pydantic import BaseModel, Field
from .utils import _default_if_none
from .utils import _exclude_if
from .v1_container_state_running import V1ContainerStateRunning
from .v1_container_state_terminated import V1ContainerStateTerminated
from .v1_container_state_waiting import V1ContainerStateWaiting
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1ContainerState",)


class V1ContainerState(BaseModel):
    running: Annotated[
        V1ContainerStateRunning,
        BeforeValidator(_default_if_none(V1ContainerStateRunning)),
    ] = Field(default_factory=lambda: V1ContainerStateRunning(), exclude_if=_exclude_if)

    terminated: Annotated[
        V1ContainerStateTerminated,
        BeforeValidator(_default_if_none(V1ContainerStateTerminated)),
    ] = Field(
        default_factory=lambda: V1ContainerStateTerminated(), exclude_if=_exclude_if
    )

    waiting: Annotated[
        V1ContainerStateWaiting,
        BeforeValidator(_default_if_none(V1ContainerStateWaiting)),
    ] = Field(default_factory=lambda: V1ContainerStateWaiting(), exclude_if=_exclude_if)
