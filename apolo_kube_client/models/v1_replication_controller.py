from pydantic import BaseModel, Field

from .v1_object_meta import V1ObjectMeta
from .v1_replication_controller_spec import V1ReplicationControllerSpec
from .v1_replication_controller_status import V1ReplicationControllerStatus


class V1ReplicationController(BaseModel):
    api_version: str | None = Field(None, alias="apiVersion")

    kind: str | None = Field(None, alias="kind")

    metadata: V1ObjectMeta | None = Field(None, alias="metadata")

    spec: V1ReplicationControllerSpec | None = Field(None, alias="spec")

    status: V1ReplicationControllerStatus | None = Field(None, alias="status")
