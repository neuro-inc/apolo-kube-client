from typing import Annotated, ClassVar, Final

from pydantic import Field

from .base_model import BaseConfiguredModel


__all__ = ("V1beta2Counter",)


class V1beta2Counter(BaseConfiguredModel):
    """Counter describes a quantity associated with a device."""

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.resource.v1beta2.Counter"

    value: Annotated[
        str,
        Field(
            description="""Value defines how much of a certain device counter is available."""
        ),
    ]
