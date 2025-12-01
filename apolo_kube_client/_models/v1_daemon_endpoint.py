from typing import Annotated, ClassVar, Final

from pydantic import Field

from .base_model import BaseConfiguredModel


__all__ = ("V1DaemonEndpoint",)


class V1DaemonEndpoint(BaseConfiguredModel):
    """DaemonEndpoint contains information about a single Daemon endpoint."""

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.core.v1.DaemonEndpoint"

    port: Annotated[
        int, Field(alias="Port", description="""Port number of the given endpoint.""")
    ]
