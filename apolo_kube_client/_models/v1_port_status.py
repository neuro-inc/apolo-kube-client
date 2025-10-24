from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field


__all__ = ("V1PortStatus",)


class V1PortStatus(BaseModel):
    """PortStatus represents the error condition of a service port"""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.core.v1.PortStatus"

    error: Annotated[
        str | None,
        Field(
            description="""Error is to record the problem with the service port The format of the error shall comply with the following rules: - built-in error values shall be specified in this file and those shall use
  CamelCase names
- cloud provider specific error values must have names that comply with the
  format foo.example.com/CamelCase.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    port: Annotated[
        int,
        Field(
            description="""Port is the port number of the service port of which status is recorded here"""
        ),
    ]

    protocol: Annotated[
        str,
        Field(
            description='''Protocol is the protocol of the service port of which status is recorded here The supported values are: "TCP", "UDP", "SCTP"'''
        ),
    ]
