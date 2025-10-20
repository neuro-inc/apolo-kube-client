from pydantic import AliasChoices, Field
from .base import ResourceModel
from .v1_csi_node_spec import V1CSINodeSpec
from .v1_object_meta import V1ObjectMeta

__all__ = ("V1CSINode",)


class V1CSINode(ResourceModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
    )

    kind: str | None = None

    metadata: V1ObjectMeta = Field(default_factory=lambda: V1ObjectMeta())

    spec: V1CSINodeSpec = Field(default_factory=lambda: V1CSINodeSpec())
