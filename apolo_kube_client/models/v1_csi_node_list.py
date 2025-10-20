from pydantic import AliasChoices, Field
from .base import ListModel
from .v1_csi_node import V1CSINode
from .v1_list_meta import V1ListMeta

__all__ = ("V1CSINodeList",)


class V1CSINodeList(ListModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
    )

    items: list[V1CSINode] = []

    kind: str | None = None

    metadata: V1ListMeta = Field(default_factory=lambda: V1ListMeta())
