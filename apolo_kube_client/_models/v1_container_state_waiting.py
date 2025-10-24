from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field


__all__ = ("V1ContainerStateWaiting",)


class V1ContainerStateWaiting(BaseModel):
    """ContainerStateWaiting is a waiting state of a container."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.core.v1.ContainerStateWaiting"

    message: Annotated[
        str | None,
        Field(
            description="""Message regarding why the container is not yet running.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    reason: Annotated[
        str | None,
        Field(
            description="""(brief) reason the container is not yet running.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None
