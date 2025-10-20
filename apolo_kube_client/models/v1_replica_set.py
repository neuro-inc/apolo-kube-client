from pydantic import AliasChoices, Field
from .base import ResourceModel
from .v1_object_meta import V1ObjectMeta
from .v1_replica_set_spec import V1ReplicaSetSpec
from .v1_replica_set_status import V1ReplicaSetStatus

__all__ = ("V1ReplicaSet",)


class V1ReplicaSet(ResourceModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
    )

    kind: str | None = None

    metadata: V1ObjectMeta = Field(default_factory=lambda: V1ObjectMeta())

    spec: V1ReplicaSetSpec = Field(default_factory=lambda: V1ReplicaSetSpec())

    status: V1ReplicaSetStatus = Field(default_factory=lambda: V1ReplicaSetStatus())
