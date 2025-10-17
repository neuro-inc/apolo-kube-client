from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field
from .v1_csi_node import V1CSINode
from .v1_list_meta import V1ListMeta

__all__ = ("V1CSINodeList",)


class V1CSINodeList(BaseModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
    )

    items: list[V1CSINode] = Field(default=[])

    kind: str | None = Field(default=None)

    metadata: V1ListMeta
