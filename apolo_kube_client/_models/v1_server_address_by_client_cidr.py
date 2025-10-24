from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field


__all__ = ("V1ServerAddressByClientCIDR",)


class V1ServerAddressByClientCIDR(BaseModel):
    """ServerAddressByClientCIDR helps the client to determine the server address that they should use, depending on the clientCIDR that they match."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = (
        "io.k8s.apimachinery.pkg.apis.meta.v1.ServerAddressByClientCIDR"
    )

    client_cidr: Annotated[
        str,
        Field(
            alias="clientCIDR",
            description="""The CIDR with which clients can match their IP to figure out the server address that they should use.""",
        ),
    ]

    server_address: Annotated[
        str,
        Field(
            alias="serverAddress",
            description="""Address of this server, suitable for a client that matches the above CIDR. This can be a hostname, hostname:port, IP or IP:port.""",
        ),
    ]
