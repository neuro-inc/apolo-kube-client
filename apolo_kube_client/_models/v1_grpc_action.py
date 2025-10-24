from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field


__all__ = ("V1GRPCAction",)


class V1GRPCAction(BaseModel):
    """GRPCAction specifies an action involving a GRPC service."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.core.v1.GRPCAction"

    port: Annotated[
        int,
        Field(
            description="""Port number of the gRPC service. Number must be in the range 1 to 65535."""
        ),
    ]

    service: Annotated[
        str | None,
        Field(
            description="""Service is the name of the service to place in the gRPC HealthCheckRequest (see https://github.com/grpc/grpc/blob/master/doc/health-checking.md).

If this is not specified, the default behavior is defined by gRPC.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None
