from typing import Annotated, ClassVar, Final

from pydantic import BaseModel, Field


__all__ = ("V1DaemonEndpoint",)


class V1DaemonEndpoint(BaseModel):
    """DaemonEndpoint contains information about a single Daemon endpoint."""

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.core.v1.DaemonEndpoint"

    port: Annotated[
        int, Field(alias="Port", description="""Port number of the given endpoint.""")
    ]
