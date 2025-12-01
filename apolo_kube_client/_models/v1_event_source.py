from typing import Annotated, ClassVar, Final

from pydantic import BaseModel, Field


__all__ = ("V1EventSource",)


class V1EventSource(BaseModel):
    """EventSource contains information for an event."""

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.core.v1.EventSource"

    component: Annotated[
        str | None,
        Field(
            description="""Component from which the event is generated.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    host: Annotated[
        str | None,
        Field(
            description="""Node name on which the event is generated.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None
