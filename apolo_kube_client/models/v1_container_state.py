from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_container_state_running import V1ContainerStateRunning
from .v1_container_state_terminated import V1ContainerStateTerminated
from .v1_container_state_waiting import V1ContainerStateWaiting

__all__ = ("V1ContainerState",)


class V1ContainerState(BaseModel):
    running: V1ContainerStateRunning = Field(
        default_factory=lambda: V1ContainerStateRunning()
    )

    terminated: V1ContainerStateTerminated = Field(
        default_factory=lambda: V1ContainerStateTerminated()
    )

    waiting: V1ContainerStateWaiting = Field(
        default_factory=lambda: V1ContainerStateWaiting()
    )
