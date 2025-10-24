from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from datetime import datetime

__all__ = ("V1ContainerStateRunning",)


class V1ContainerStateRunning(BaseModel):
    """ContainerStateRunning is a running state of a container."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.core.v1.ContainerStateRunning"

    started_at: Annotated[
        datetime | None,
        Field(
            alias="startedAt",
            description="""Time at which the container was last (re-)started""",
            exclude_if=lambda v: v is None,
        ),
    ] = None
