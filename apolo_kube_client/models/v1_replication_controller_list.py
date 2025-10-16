from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_list_meta import V1ListMeta
from .v1_replication_controller import V1ReplicationController

__all__ = ("V1ReplicationControllerList",)


class V1ReplicationControllerList(BaseModel):
    api_version: str | None = Field(default_factory=lambda: None, alias="apiVersion")

    items: list[V1ReplicationController] = Field(
        default_factory=lambda: [], alias="items"
    )

    kind: str | None = Field(default_factory=lambda: None, alias="kind")

    metadata: V1ListMeta = Field(default_factory=lambda: V1ListMeta(), alias="metadata")
