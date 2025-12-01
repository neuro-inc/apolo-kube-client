from typing import Annotated, ClassVar, Final

from pydantic import BaseModel, Field


__all__ = ("V1NodeSwapStatus",)


class V1NodeSwapStatus(BaseModel):
    """NodeSwapStatus represents swap memory information."""

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.core.v1.NodeSwapStatus"

    capacity: Annotated[
        int | None,
        Field(
            description="""Total amount of swap memory in bytes.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None
