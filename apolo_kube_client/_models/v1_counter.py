from typing import Annotated, ClassVar, Final

from pydantic import BaseModel, Field


__all__ = ("V1Counter",)


class V1Counter(BaseModel):
    """Counter describes a quantity associated with a device."""

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.resource.v1.Counter"

    value: Annotated[
        str,
        Field(
            description="""Value defines how much of a certain device counter is available."""
        ),
    ]
