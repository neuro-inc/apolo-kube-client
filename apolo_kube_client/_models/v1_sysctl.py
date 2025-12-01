from typing import Annotated, ClassVar, Final

from pydantic import Field

from .base_model import BaseConfiguredModel


__all__ = ("V1Sysctl",)


class V1Sysctl(BaseConfiguredModel):
    """Sysctl defines a kernel parameter to be set"""

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.core.v1.Sysctl"

    name: Annotated[str, Field(description="""Name of a property to set""")]

    value: Annotated[str, Field(description="""Value of a property to set""")]
