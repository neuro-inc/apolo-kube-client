from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field
from .v1_list_meta import V1ListMeta
from .v1_replica_set import V1ReplicaSet

__all__ = ("V1ReplicaSetList",)


class V1ReplicaSetList(BaseModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
    )

    items: list[V1ReplicaSet] = Field(default=[])

    kind: str | None = Field(default=None)

    metadata: V1ListMeta
