from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from .utils import _default_if_none
from .v1_node_selector import V1NodeSelector
from pydantic import BeforeValidator

__all__ = ("V1VolumeNodeAffinity",)


class V1VolumeNodeAffinity(BaseModel):
    """VolumeNodeAffinity defines constraints that limit what nodes this volume can be accessed from."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.core.v1.VolumeNodeAffinity"

    required: Annotated[
        V1NodeSelector | None,
        Field(
            description="""required specifies hard node constraints that must be met.""",
            exclude_if=lambda v: v is None,
        ),
        BeforeValidator(_default_if_none(V1NodeSelector)),
    ] = None
