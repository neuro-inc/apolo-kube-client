from typing import Annotated, ClassVar, Final

from pydantic import Field

from .base_model import BaseConfiguredModel


__all__ = ("V1NodeAddress",)


class V1NodeAddress(BaseConfiguredModel):
    """NodeAddress contains information for the node's address."""

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.core.v1.NodeAddress"

    address: Annotated[str, Field(description="""The node address.""")]

    type: Annotated[
        str,
        Field(
            description="""Node address type, one of Hostname, ExternalIP or InternalIP."""
        ),
    ]
