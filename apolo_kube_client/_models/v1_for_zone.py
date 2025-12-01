from typing import Annotated, ClassVar, Final

from pydantic import BaseModel, Field


__all__ = ("V1ForZone",)


class V1ForZone(BaseModel):
    """ForZone provides information about which zones should consume this endpoint."""

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.discovery.v1.ForZone"

    name: Annotated[str, Field(description="""name represents the name of the zone.""")]
