from __future__ import annotations

from pydantic import BaseModel, Field

from .v1_list_meta import V1ListMeta
from .v1_replica_set import V1ReplicaSet

__all__ = ("V1ReplicaSetList",)


class V1ReplicaSetList(BaseModel):
    api_version: str | None = Field(None, alias="apiVersion")

    items: list[V1ReplicaSet] | None = Field(None, alias="items")

    kind: str | None = Field(None, alias="kind")

    metadata: V1ListMeta | None = Field(None, alias="metadata")
