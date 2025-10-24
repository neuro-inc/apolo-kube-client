from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field


__all__ = ("V1IngressPortStatus",)


class V1IngressPortStatus(BaseModel):
    """IngressPortStatus represents the error condition of a service port"""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.networking.v1.IngressPortStatus"

    error: Annotated[
        str | None,
        Field(
            description="""error is to record the problem with the service port The format of the error shall comply with the following rules: - built-in error values shall be specified in this file and those shall use
  CamelCase names
- cloud provider specific error values must have names that comply with the
  format foo.example.com/CamelCase.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    port: Annotated[
        int, Field(description="""port is the port number of the ingress port.""")
    ]

    protocol: Annotated[
        str,
        Field(
            description='''protocol is the protocol of the ingress port. The supported values are: "TCP", "UDP", "SCTP"'''
        ),
    ]
