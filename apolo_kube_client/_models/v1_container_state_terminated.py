from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from datetime import datetime

__all__ = ("V1ContainerStateTerminated",)


class V1ContainerStateTerminated(BaseModel):
    """ContainerStateTerminated is a terminated state of a container."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.core.v1.ContainerStateTerminated"

    container_id: Annotated[
        str | None,
        Field(
            alias="containerID",
            description="""Container's ID in the format '<type>://<container_id>'""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    exit_code: Annotated[
        int,
        Field(
            alias="exitCode",
            description="""Exit status from the last termination of the container""",
        ),
    ]

    finished_at: Annotated[
        datetime | None,
        Field(
            alias="finishedAt",
            description="""Time at which the container last terminated""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    message: Annotated[
        str | None,
        Field(
            description="""Message regarding the last termination of the container""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    reason: Annotated[
        str | None,
        Field(
            description="""(brief) reason from the last termination of the container""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    signal: Annotated[
        int | None,
        Field(
            description="""Signal from the last termination of the container""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    started_at: Annotated[
        datetime | None,
        Field(
            alias="startedAt",
            description="""Time at which previous execution of the container started""",
            exclude_if=lambda v: v is None,
        ),
    ] = None
