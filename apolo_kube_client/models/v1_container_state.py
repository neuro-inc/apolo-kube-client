from __future__ import annotations

from pydantic import BaseModel, Field

from .v1_container_state_running import V1ContainerStateRunning
from .v1_container_state_terminated import V1ContainerStateTerminated
from .v1_container_state_waiting import V1ContainerStateWaiting

__all__ = ("V1ContainerState",)


class V1ContainerState(BaseModel):
    running: V1ContainerStateRunning | None = Field(None, alias="running")

    terminated: V1ContainerStateTerminated | None = Field(None, alias="terminated")

    waiting: V1ContainerStateWaiting | None = Field(None, alias="waiting")
