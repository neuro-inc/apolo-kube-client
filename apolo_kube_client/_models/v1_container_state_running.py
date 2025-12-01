from datetime import datetime
from typing import Annotated, ClassVar, Final

from pydantic import Field

from .base_model import BaseConfiguredModel


__all__ = ("V1ContainerStateRunning",)


class V1ContainerStateRunning(BaseConfiguredModel):
    """ContainerStateRunning is a running state of a container."""

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.core.v1.ContainerStateRunning"

    started_at: Annotated[
        datetime | None,
        Field(
            alias="startedAt",
            description="""Time at which the container was last (re-)started""",
            exclude_if=lambda v: v is None,
        ),
    ] = None
