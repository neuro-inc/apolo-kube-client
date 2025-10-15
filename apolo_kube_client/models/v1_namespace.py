from pydantic import BaseModel, Field

from .v1_namespace_spec import V1NamespaceSpec
from .v1_namespace_status import V1NamespaceStatus
from .v1_object_meta import V1ObjectMeta


class V1Namespace(BaseModel):
    api_version: str | None = Field(None, alias="apiVersion")

    kind: str | None = Field(None, alias="kind")

    metadata: V1ObjectMeta | None = Field(None, alias="metadata")

    spec: V1NamespaceSpec | None = Field(None, alias="spec")

    status: V1NamespaceStatus | None = Field(None, alias="status")
