from typing import Annotated, ClassVar, Final

from pydantic import Field

from .base_model import BaseConfiguredModel


__all__ = ("V1ForNode",)


class V1ForNode(BaseConfiguredModel):
    """ForNode provides information about which nodes should consume this endpoint."""

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.discovery.v1.ForNode"

    name: Annotated[str, Field(description="""name represents the name of the node.""")]
