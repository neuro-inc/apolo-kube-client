from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field
from .v1_csi_node_spec import V1CSINodeSpec
from .v1_object_meta import V1ObjectMeta

__all__ = ("V1CSINode",)


class V1CSINode(BaseModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
    )

    kind: str | None = Field(default=None)

    metadata: V1ObjectMeta

    spec: V1CSINodeSpec = Field(default_factory=lambda: V1CSINodeSpec())
