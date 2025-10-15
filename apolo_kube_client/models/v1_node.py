from pydantic import BaseModel, Field

from .v1_node_spec import V1NodeSpec
from .v1_node_status import V1NodeStatus
from .v1_object_meta import V1ObjectMeta


class V1Node(BaseModel):
    api_version: str | None = Field(None, alias="apiVersion")

    kind: str | None = Field(None, alias="kind")

    metadata: V1ObjectMeta | None = Field(None, alias="metadata")

    spec: V1NodeSpec | None = Field(None, alias="spec")

    status: V1NodeStatus | None = Field(None, alias="status")
