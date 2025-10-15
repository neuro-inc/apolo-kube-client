from pydantic import BaseModel, Field

from .v1_daemon_set_spec import V1DaemonSetSpec
from .v1_daemon_set_status import V1DaemonSetStatus
from .v1_object_meta import V1ObjectMeta


class V1DaemonSet(BaseModel):
    api_version: str | None = Field(None, alias="apiVersion")

    kind: str | None = Field(None, alias="kind")

    metadata: V1ObjectMeta | None = Field(None, alias="metadata")

    spec: V1DaemonSetSpec | None = Field(None, alias="spec")

    status: V1DaemonSetStatus | None = Field(None, alias="status")
