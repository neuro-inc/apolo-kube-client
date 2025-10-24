from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field


__all__ = ("V1NodeAddress",)


class V1NodeAddress(BaseModel):
    """NodeAddress contains information for the node's address."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.core.v1.NodeAddress"

    address: Annotated[str, Field(description="""The node address.""")]

    type: Annotated[
        str,
        Field(
            description="""Node address type, one of Hostname, ExternalIP or InternalIP."""
        ),
    ]
