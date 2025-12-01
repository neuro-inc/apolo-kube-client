from typing import Annotated, ClassVar, Final

from pydantic import Field

from .base_model import BaseConfiguredModel


__all__ = ("V1ForZone",)


class V1ForZone(BaseConfiguredModel):
    """ForZone provides information about which zones should consume this endpoint."""

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.discovery.v1.ForZone"

    name: Annotated[str, Field(description="""name represents the name of the zone.""")]
