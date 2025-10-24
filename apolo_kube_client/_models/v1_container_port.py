from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field


__all__ = ("V1ContainerPort",)


class V1ContainerPort(BaseModel):
    """ContainerPort represents a network port in a single container."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.core.v1.ContainerPort"

    container_port: Annotated[
        int,
        Field(
            alias="containerPort",
            description="""Number of port to expose on the pod's IP address. This must be a valid port number, 0 < x < 65536.""",
        ),
    ]

    host_ip: Annotated[
        str | None,
        Field(
            alias="hostIP",
            description="""What host IP to bind the external port to.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    host_port: Annotated[
        int | None,
        Field(
            alias="hostPort",
            description="""Number of port to expose on the host. If specified, this must be a valid port number, 0 < x < 65536. If HostNetwork is specified, this must match ContainerPort. Most containers do not need this.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    name: Annotated[
        str | None,
        Field(
            description="""If specified, this must be an IANA_SVC_NAME and unique within the pod. Each named port in a pod must have a unique name. Name for the port that can be referred to by services.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    protocol: Annotated[
        str | None,
        Field(
            description="""Protocol for port. Must be UDP, TCP, or SCTP. Defaults to "TCP".""",
            exclude_if=lambda v: v is None,
        ),
    ] = None
