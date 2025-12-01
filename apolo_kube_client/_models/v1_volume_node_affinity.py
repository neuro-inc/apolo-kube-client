from typing import Annotated, ClassVar, Final

from pydantic import Field

from .base_model import BaseConfiguredModel
from .v1_node_selector import V1NodeSelector


__all__ = ("V1VolumeNodeAffinity",)


class V1VolumeNodeAffinity(BaseConfiguredModel):
    """VolumeNodeAffinity defines constraints that limit what nodes this volume can be accessed from."""

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.core.v1.VolumeNodeAffinity"

    required: Annotated[
        V1NodeSelector | None,
        Field(
            description="""required specifies hard node constraints that must be met.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None
