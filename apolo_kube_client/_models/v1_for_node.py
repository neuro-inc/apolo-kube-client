from typing import Annotated, ClassVar, Final

from pydantic import BaseModel, Field


__all__ = ("V1ForNode",)


class V1ForNode(BaseModel):
    """ForNode provides information about which nodes should consume this endpoint."""

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.discovery.v1.ForNode"

    name: Annotated[str, Field(description="""name represents the name of the node.""")]
