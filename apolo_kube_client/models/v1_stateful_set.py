from pydantic import BaseModel, Field

from .v1_object_meta import V1ObjectMeta
from .v1_stateful_set_spec import V1StatefulSetSpec
from .v1_stateful_set_status import V1StatefulSetStatus


class V1StatefulSet(BaseModel):
    api_version: str | None = Field(None, alias="apiVersion")

    kind: str | None = Field(None, alias="kind")

    metadata: V1ObjectMeta | None = Field(None, alias="metadata")

    spec: V1StatefulSetSpec | None = Field(None, alias="spec")

    status: V1StatefulSetStatus | None = Field(None, alias="status")
