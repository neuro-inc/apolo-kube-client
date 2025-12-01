from typing import Annotated, ClassVar, Final

from pydantic import BaseModel, Field


__all__ = ("V1PodSchedulingGate",)


class V1PodSchedulingGate(BaseModel):
    """PodSchedulingGate is associated to a Pod to guard its scheduling."""

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.core.v1.PodSchedulingGate"

    name: Annotated[
        str,
        Field(
            description="""Name of the scheduling gate. Each scheduling gate must have a unique name field."""
        ),
    ]
