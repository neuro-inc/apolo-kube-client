from typing import Annotated, ClassVar, Final

from pydantic import Field

from .base_model import BaseConfiguredModel
from .v1_container_state_running import V1ContainerStateRunning
from .v1_container_state_terminated import V1ContainerStateTerminated
from .v1_container_state_waiting import V1ContainerStateWaiting


__all__ = ("V1ContainerState",)


class V1ContainerState(BaseConfiguredModel):
    """ContainerState holds a possible state of container. Only one of its members may be specified. If none of them is specified, the default one is ContainerStateWaiting."""

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.core.v1.ContainerState"

    running: Annotated[
        V1ContainerStateRunning | None,
        Field(
            description="""Details about a running container""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    terminated: Annotated[
        V1ContainerStateTerminated | None,
        Field(
            description="""Details about a terminated container""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    waiting: Annotated[
        V1ContainerStateWaiting | None,
        Field(
            description="""Details about a waiting container""",
            exclude_if=lambda v: v is None,
        ),
    ] = None
