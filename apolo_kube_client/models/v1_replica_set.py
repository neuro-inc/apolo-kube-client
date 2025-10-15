from pydantic import BaseModel, Field

from .v1_object_meta import V1ObjectMeta
from .v1_replica_set_spec import V1ReplicaSetSpec
from .v1_replica_set_status import V1ReplicaSetStatus


class V1ReplicaSet(BaseModel):
    api_version: str | None = Field(None, alias="apiVersion")

    kind: str | None = Field(None, alias="kind")

    metadata: V1ObjectMeta | None = Field(None, alias="metadata")

    spec: V1ReplicaSetSpec | None = Field(None, alias="spec")

    status: V1ReplicaSetStatus | None = Field(None, alias="status")
