from __future__ import annotations

from pydantic import BaseModel, Field

from .v1_flow_schema import V1FlowSchema
from .v1_list_meta import V1ListMeta

__all__ = ("V1FlowSchemaList",)


class V1FlowSchemaList(BaseModel):
    api_version: str | None = Field(None, alias="apiVersion")

    items: list[V1FlowSchema] | None = Field(None, alias="items")

    kind: str | None = Field(None, alias="kind")

    metadata: V1ListMeta | None = Field(None, alias="metadata")
