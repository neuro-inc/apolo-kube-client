from pydantic import BaseModel, Field

from .v1_object_meta import V1ObjectMeta
from .v1_pod_spec import V1PodSpec
from .v1_pod_status import V1PodStatus


class V1Pod(BaseModel):
    api_version: str | None = Field(None, alias="apiVersion")

    kind: str | None = Field(None, alias="kind")

    metadata: V1ObjectMeta | None = Field(None, alias="metadata")

    spec: V1PodSpec | None = Field(None, alias="spec")

    status: V1PodStatus | None = Field(None, alias="status")
