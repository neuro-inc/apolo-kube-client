from __future__ import annotations

from pydantic import BaseModel, Field

from .v1_flow_schema_spec import V1FlowSchemaSpec
from .v1_flow_schema_status import V1FlowSchemaStatus
from .v1_object_meta import V1ObjectMeta

__all__ = ("V1FlowSchema",)


class V1FlowSchema(BaseModel):
    api_version: str | None = Field(None, alias="apiVersion")

    kind: str | None = Field(None, alias="kind")

    metadata: V1ObjectMeta | None = Field(None, alias="metadata")

    spec: V1FlowSchemaSpec | None = Field(None, alias="spec")

    status: V1FlowSchemaStatus | None = Field(None, alias="status")
