from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_csi_node_spec import V1CSINodeSpec
from .v1_object_meta import V1ObjectMeta

__all__ = ("V1CSINode",)


class V1CSINode(BaseModel):
    api_version: str | None = Field(default_factory=lambda: None, alias="apiVersion")

    kind: str | None = Field(default_factory=lambda: None, alias="kind")

    metadata: V1ObjectMeta = Field(
        default_factory=lambda: V1ObjectMeta(), alias="metadata"
    )

    spec: V1CSINodeSpec = Field(default_factory=lambda: V1CSINodeSpec(), alias="spec")
