from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field


__all__ = ("V1DaemonEndpoint",)


class V1DaemonEndpoint(BaseModel):
    """DaemonEndpoint contains information about a single Daemon endpoint."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.core.v1.DaemonEndpoint"

    port: Annotated[
        int, Field(alias="Port", description="""Port number of the given endpoint.""")
    ]
