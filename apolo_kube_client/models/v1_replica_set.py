from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field
from .v1_object_meta import V1ObjectMeta
from .v1_replica_set_spec import V1ReplicaSetSpec
from .v1_replica_set_status import V1ReplicaSetStatus

__all__ = ("V1ReplicaSet",)


class V1ReplicaSet(BaseModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
    )

    kind: str | None = Field(default=None)

    metadata: V1ObjectMeta

    spec: V1ReplicaSetSpec = Field(default_factory=lambda: V1ReplicaSetSpec())

    status: V1ReplicaSetStatus = Field(default_factory=lambda: V1ReplicaSetStatus())
