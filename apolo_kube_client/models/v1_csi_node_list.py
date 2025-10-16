from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_csi_node import V1CSINode
from .v1_list_meta import V1ListMeta

__all__ = ("V1CSINodeList",)


class V1CSINodeList(BaseModel):
    api_version: str | None = Field(default_factory=lambda: None, alias="apiVersion")

    items: list[V1CSINode] = Field(default_factory=lambda: [], alias="items")

    kind: str | None = Field(default_factory=lambda: None, alias="kind")

    metadata: V1ListMeta = Field(default_factory=lambda: V1ListMeta(), alias="metadata")
